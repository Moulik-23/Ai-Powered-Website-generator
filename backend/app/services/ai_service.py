import google.generativeai as genai
import os
import json
from typing import Dict, List
from dotenv import load_dotenv
from pathlib import Path
from ..templates.components import COMPONENTS, COMMON_JS
from ..templates.color_schemes import COLOR_SCHEMES

# Load .env from backend directory
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class AIService:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    async def generate_website(
        self, 
        prompt: str, 
        style: str = "modern",
        color_scheme: str = "default"
    ) -> Dict:
        """
        Generate a complete website based on user prompt
        """
        
        # Analyze the prompt to determine components needed
        components_analysis = await self._analyze_prompt(prompt)
        
        # Generate content for each component
        components_data = await self._generate_components(
            prompt, 
            components_analysis,
            style
        )
        
        # Generate meta information
        meta_info = await self._generate_meta_info(prompt)
        
        # Assemble the full website
        html = self._assemble_html(components_data, meta_info, style, color_scheme)
        css = self._assemble_css(components_data, color_scheme)
        js = COMMON_JS
        
        return {
            "html": html,
            "css": css,
            "js": js,
            "components": components_data,
            "meta_description": meta_info["description"],
            "title": meta_info["title"],
            "prompt": prompt,
            "style": style,
            "color_scheme": color_scheme
        }
    
    async def _analyze_prompt(self, prompt: str) -> Dict:
        """
        Analyze user prompt to determine which components are needed
        """
        analysis_prompt = f"""
Analyze this website request and determine which components are needed:
"{prompt}"

Available components: navigation, hero, features, gallery, contact, footer

Return ONLY a JSON object with this structure:
{{
    "components": ["component1", "component2", ...],
    "website_type": "portfolio|business|ecommerce|blog|landing",
    "primary_focus": "brief description"
}}

Example response:
{{"components": ["navigation", "hero", "features", "gallery", "contact", "footer"], "website_type": "portfolio", "primary_focus": "photography showcase"}}
"""
        
        try:
            response = self.model.generate_content(analysis_prompt)
            # Extract JSON from response
            text = response.text.strip()
            
            # Remove markdown code blocks if present
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[1].split("```")[0].strip()
            
            # Try to find JSON in the response
            start_idx = text.find('{')
            end_idx = text.rfind('}') + 1
            
            if start_idx != -1 and end_idx > start_idx:
                json_str = text[start_idx:end_idx]
                try:
                    analysis = json.loads(json_str)
                except json.JSONDecodeError:
                    print(f"JSON decode error in analysis: {json_str[:100]}...")
                    analysis = self._heuristic_analyze(prompt)
            else:
                # Heuristic fallback
                print(f"No JSON found in analysis response: {text[:100]}...")
                analysis = self._heuristic_analyze(prompt)
            
            return analysis
        except Exception as e:
            print(f"Error in analysis: {e}")
            # Heuristic fallback
            return self._heuristic_analyze(prompt)

    def _heuristic_analyze(self, prompt: str) -> Dict:
        """Derive components and website type from prompt without AI"""
        p = prompt.lower()
        website_type = self._infer_website_type(p)

        # Choose components by website type
        components = ["navigation", "hero"]
        if website_type in ("portfolio", "blog"):
            components += ["features", "gallery"]
        else:
            components += ["features"]
        components += ["contact", "footer"]

        # Primary focus derived from role/keywords
        primary_focus = self._extract_role(prompt) or "general purpose"

        return {
            "components": components,
            "website_type": website_type,
            "primary_focus": primary_focus
        }
    
    async def _generate_components(
        self, 
        prompt: str, 
        analysis: Dict,
        style: str
    ) -> List[Dict]:
        """
        Generate content for each component
        """
        components_data = []
        component_list = analysis.get("components", [])
        website_type = analysis.get("website_type", self._infer_website_type(prompt))
        
        for component_type in component_list:
            if component_type not in COMPONENTS:
                continue
            
            content = await self._generate_component_content(
                prompt,
                component_type,
                website_type,
                style
            )
            
            components_data.append({
                "type": component_type,
                "html": content["html"],
                "css": COMPONENTS[component_type].get("css", ""),
                "js": content.get("js", "")
            })
        
        return components_data
    
    async def _generate_component_content(
        self,
        prompt: str,
        component_type: str,
        website_type: str,
        style: str
    ) -> Dict:
        """
        Generate specific content for a component using AI
        """
        template = COMPONENTS[component_type][style]
        
        content_prompt = f"""
You are a professional web content creator. Generate content for a {component_type} component.

Website description: "{prompt}"
Website type: {website_type}
Design style: {style}

Create realistic, specific, and relevant content based on the prompt. Use details from the prompt to make the content unique and appropriate.

Return ONLY a valid JSON object with these fields (adjust based on component type):
- For navigation: brand_name, nav_items (as HTML list items)
- For hero: title, subtitle, cta_buttons (as HTML buttons)
- For features: section_title, section_subtitle, feature_items (as HTML divs)
- For gallery: section_title, gallery_items (as HTML divs)
- For contact: section_title, section_subtitle
- For footer: brand_name, brand_description, year, footer_sections (as HTML)

IMPORTANT: Make content SPECIFIC to this website type and prompt. Do not use generic placeholders.
Example response format:
{{"section_title": "Specific Title Based on Prompt", "section_subtitle": "Specific subtitle", "feature_items": "<div>...</div>"}}

RESPOND WITH ONLY THE JSON, NO OTHER TEXT:
"""
        
        try:
            response = self.model.generate_content(content_prompt)
            text = response.text.strip()
            
            # Extract JSON - be more flexible with parsing
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[1].split("```")[0].strip()

            start_idx = text.find('{')
            end_idx = text.rfind('}') + 1
            
            if start_idx != -1 and end_idx > start_idx:
                json_str = text[start_idx:end_idx]
                try:
                    content_data = json.loads(json_str)
                except json.JSONDecodeError as je:
                    print(f"JSON parse error for {component_type}: {je}")
                    print(f"Response was: {json_str[:200]}")
                    content_data = self._get_default_content(component_type, prompt)
            else:
                print(f"No JSON found in response for {component_type}")
                content_data = self._get_default_content(component_type, prompt)
            
            # Fill template with content
            html = self._fill_template(template, content_data, component_type)
            
            return {"html": html, "js": ""}
        
        except Exception as e:
            print(f"Error generating component content for {component_type}: {e}")
            import traceback
            traceback.print_exc()
            content_data = self._get_default_content(component_type, prompt)
            html = self._fill_template(template, content_data, component_type)
            return {"html": html, "js": ""}
    
    def _get_default_content(self, component_type: str, prompt: str) -> Dict:
        """
        Get content for components when AI generation fails - extract from prompt
        """
        p = prompt.lower()
        website_type = self._infer_website_type(p)
        role = self._extract_role(prompt) or "professional"
        is_portfolio = website_type == "portfolio"
        is_blog = website_type == "blog"

        defaults = {
            "navigation": {
                "brand_name": self._extract_brand_name(prompt),
                "nav_items": """
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#contact">Contact</a></li>
                """
            },
            "hero": {
                "title": self._compose_title(role, website_type),
                "subtitle": self._compose_subtitle(role, website_type),
                "cta_buttons": """
                    <button class=\"btn btn-primary\">Get Started</button>
                    <button class=\"btn btn-secondary\">Learn More</button>
                """,
                "hero_image": '<div style="width: 100%; height: 400px; background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--accent) 100%); border-radius: 12px; display: flex; align-items: center; justify-content: center;"><span style="font-size: 4rem; opacity: 0.5;">✨</span></div>'

            },
            "features": {
                "section_title": "Key Features" if not is_blog else "Highlights",
                "section_subtitle": "What makes us unique" if not is_blog else "What you'll find here",
                "feature_items": """
                    <div class=\"feature-card\">\n                        <div class=\"feature-icon\">&#128640;</div>\n                        <h3>Fast & Efficient</h3>\n                        <p>Lightning-fast performance optimized for your needs</p>\n                    </div>\n                    <div class=\"feature-card\">\n                        <div class=\"feature-icon\">&#127912;</div>\n                        <h3>Beautiful Design</h3>\n                        <p>Modern, clean design that captures attention</p>\n                    </div>\n                    <div class=\"feature-card\">\n                        <div class=\"feature-icon\">&#128274;</div>\n                        <h3>Secure & Reliable</h3>\n                        <p>Enterprise-grade security and reliability</p>\n                    </div>
                """
            },
            "gallery": {
                "section_title": "Portfolio" if is_portfolio else ("Recent Posts" if is_blog else "Gallery"),
                "gallery_items": """
                    <div class=\"gallery-item\">\n                        <img src=\"https://via.placeholder.com/400x300/667eea/ffffff?text=Project+1\" alt=\"Project 1\">\n                        <div class=\"gallery-overlay\"><h3>Project 1</h3></div>\n                    </div>\n                    <div class=\"gallery-item\">\n                        <img src=\"https://via.placeholder.com/400x300/764ba2/ffffff?text=Project+2\" alt=\"Project 2\">\n                        <div class=\"gallery-overlay\"><h3>Project 2</h3></div>\n                    </div>\n                    <div class=\"gallery-item\">\n                        <img src=\"https://via.placeholder.com/400x300/f093fb/ffffff?text=Project+3\" alt=\"Project 3\">\n                        <div class=\"gallery-overlay\"><h3>Project 3</h3></div>\n                    </div>
                """
            },
            "contact": {
                "section_title": "Get In Touch",
                "section_subtitle": "Work with us on your next project" if not is_blog else "Questions or collaboration ideas?"
            },
            "footer": {
                "brand_name": self._extract_brand_name(prompt),
                "brand_description": f"{role.title()} — {self._extract_service(prompt)}",
                "year": "2026",
                "footer_sections": """
                    <div class=\"footer-section\">\n                        <h4>Company</h4>\n                        <ul>\n                            <li><a href=\"#\">About Us</a></li>\n                            <li><a href=\"#\">Services</a></li>\n                            <li><a href=\"#\">Blog</a></li>\n                        </ul>\n                    </div>\n                    <div class=\"footer-section\">\n                        <h4>Support</h4>\n                        <ul>\n                            <li><a href=\"#\">Contact</a></li>\n                            <li><a href=\"#\">FAQ</a></li>\n                            <li><a href=\"#\">Documentation</a></li>\n                        </ul>\n                    </div>
                """
            }
        }

        return defaults.get(component_type, {})
    
    def _extract_brand_name(self, prompt: str) -> str:
        """Extract a brand name from the prompt"""
        # Simple heuristic: use first significant word or common pattern
        words = prompt.split()
        if len(words) > 0:
            return words[0].capitalize()
        return "My Website"
    
    def _extract_title(self, prompt: str) -> str:
        """Extract a title from the prompt"""
        # Take first 80 chars or first sentence
        if "." in prompt:
            return prompt.split(".")[0].strip()
        return prompt[:80].strip()
    
    def _extract_subtitle(self, prompt: str) -> str:
        """Extract a subtitle from the prompt"""
        if "for" in prompt.lower():
            parts = prompt.lower().split("for")
            if len(parts) > 1:
                return f"Specialized for {parts[1].strip()}"
        return "Professional solutions for your needs"
    
    def _extract_service(self, prompt: str) -> str:
        """Extract what service/product is offered"""
        if "mobile" in prompt.lower():
            return "mobile development"
        elif "software" in prompt.lower():
            return "software solutions"
        elif "portfolio" in prompt.lower():
            return "portfolio services"
        elif "blog" in prompt.lower():
            return "content creation"
        return "professional services"

    def _infer_website_type(self, p: str) -> str:
        """Infer website type from prompt string (already lowercased or not)"""
        pl = p.lower() if not p.islower() else p
        if any(k in pl for k in ["portfolio", "photographer", "designer", "developer portfolio"]):
            return "portfolio"
        if any(k in pl for k in ["blog", "writer", "journal", "articles"]):
            return "blog"
        if any(k in pl for k in ["shop", "store", "ecommerce", "products"]):
            return "ecommerce"
        if any(k in pl for k in ["landing", "launch", "signup"]):
            return "landing"
        return "business"

    def _extract_role(self, prompt: str) -> str:
        """Small heuristic to extract the role or subject from prompt"""
        pl = prompt.lower()
        candidates = [
            ("mobile developer", ["mobile developer", "android developer", "ios developer"]),
            ("software developer", ["software developer", "software engineer", "full stack developer", "backend developer", "frontend developer"]),
            ("photographer", ["photographer", "photography"]),
            ("travel writer", ["travel writer", "travel blogger"]),
            ("restaurant", ["restaurant", "cafe", "bistro"]),
            ("saas startup", ["saas", "startup"]),
        ]
        for label, keys in candidates:
            if any(k in pl for k in keys):
                return label
        # Fallback: use noun after "for" if present
        if " for " in pl:
            return pl.split(" for ", 1)[1].strip()
        return "professional"

    def _compose_title(self, role: str, website_type: str) -> str:
        if website_type == "portfolio":
            return f"Portfolio of a {role}"
        if website_type == "blog":
            return f"{role.title()} Blog"
        if website_type == "ecommerce":
            return f"{role.title()} Shop"
        if website_type == "landing":
            return f"{role.title()} — Modern Landing Page"
        return f"Professional {role.title()} Services"

    def _compose_subtitle(self, role: str, website_type: str) -> str:
        if website_type == "portfolio":
            return f"Showcasing recent work and case studies in {role}"
        if website_type == "blog":
            return f"Insights, tutorials, and stories from a {role}"
        if website_type == "ecommerce":
            return f"Browse curated products and resources for {role}"
        if website_type == "landing":
            return f"Clear value proposition tailored to {role}"
        return f"Tailored solutions by an experienced {role}"
    
    def _fill_template(self, template: str, content: Dict, component_type: str) -> str:
        """
        Fill template with content data
        """
        html = template
        for key, value in content.items():
            placeholder = "{" + key + "}"
            html = html.replace(placeholder, str(value))
        
        # Remove any unfilled placeholders
        import re
        html = re.sub(r'\{[^}]+\}', '', html)
        
        return html
    
    async def _generate_meta_info(self, prompt: str) -> Dict:
        """
        Generate meta information (title, description) for the website
        """
        meta_prompt = f"""
Generate SEO-friendly meta information for this website:
"{prompt}"

Return ONLY a JSON object with:
{{"title": "Page Title (max 60 chars)", "description": "Meta description (max 160 chars)"}}
"""
        
        try:
            response = self.model.generate_content(meta_prompt)
            text = response.text.strip()
            
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[1].split("```")[0].strip()

            start_idx = text.find('{')
            end_idx = text.rfind('}') + 1
            
            if start_idx != -1 and end_idx > start_idx:
                json_str = text[start_idx:end_idx]
                meta_info = json.loads(json_str)
            else:
                meta_info = {
                    "title": "My Website",
                    "description": "Welcome to our website"
                }
            
            return meta_info
        
        except Exception as e:
            print(f"Error generating meta info: {e}")
            return {
                "title": "My Website",
                "description": "Welcome to our website"
            }
    
    def _assemble_html(
        self, 
        components: List[Dict], 
        meta_info: Dict,
        style: str,
        color_scheme: str
    ) -> str:
        """
        Assemble full HTML document
        """
        components_html = "\n".join([comp["html"] for comp in components])
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{meta_info['description']}">
    <title>{meta_info['title']}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
{components_html}
    <script src="script.js"></script>
</body>
</html>"""
        
        return html
    
    def _assemble_css(self, components: List[Dict], color_scheme: str) -> str:
        """
        Assemble full CSS stylesheet
        """
        # Get color scheme variables
        scheme = COLOR_SCHEMES.get(color_scheme, COLOR_SCHEMES["default"])
        
        # Base CSS
        base_css = f"""/* Generated by AI Website Generator */
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

:root {{
{scheme['variables']}
}}

body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: var(--text-primary);
    background: var(--bg-primary);
}}

/* Utility Classes */
.btn {{
    padding: 0.75rem 2rem;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    text-decoration: none;
    display: inline-block;
}}

.btn-primary {{
    background: var(--accent);
    color: white;
}}

.btn-primary:hover {{
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}}

.btn-secondary {{
    background: transparent;
    color: var(--text-primary);
    border: 2px solid var(--accent);
}}

.btn-secondary:hover {{
    background: var(--accent);
    color: white;
}}

/* Component Styles */
"""
        
        # Add component CSS
        components_css = "\n\n".join([comp["css"] for comp in components if comp["css"]])
        
        return base_css + components_css
