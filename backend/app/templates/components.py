"""
UI Component Templates Library
Reusable components that AI can combine to generate websites
"""

COMPONENTS = {
    "navigation": {
        "modern": """
<nav class="navbar">
    <div class="nav-container">
        <div class="nav-brand">
            <h1>{brand_name}</h1>
        </div>
        <ul class="nav-menu">
            {nav_items}
        </ul>
        <button class="nav-toggle" aria-label="Toggle navigation">
            <span></span>
            <span></span>
            <span></span>
        </button>
    </div>
</nav>
""",
        "css": """
.navbar {
    background: var(--bg-primary);
    padding: 1rem 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-brand h1 {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--text-primary);
    margin: 0;
}

.nav-menu {
    display: flex;
    gap: 2rem;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-menu li a {
    color: var(--text-primary);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s;
}

.nav-menu li a:hover {
    color: var(--accent);
}

.nav-toggle {
    display: none;
    flex-direction: column;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0;
}

.nav-toggle span {
    width: 25px;
    height: 3px;
    background: var(--text-primary);
    margin: 3px 0;
    transition: 0.3s;
}

@media (max-width: 768px) {
    .nav-toggle {
        display: flex;
    }
    
    .nav-menu {
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: var(--bg-primary);
        flex-direction: column;
        padding: 2rem;
        gap: 1rem;
        display: none;
    }
    
    .nav-menu.active {
        display: flex;
    }
}
"""
    },
    
    "hero": {
        "modern": """
<section class="hero">
    <div class="hero-container">
        <div class="hero-content">
            <h1 class="hero-title">{title}</h1>
            <p class="hero-subtitle">{subtitle}</p>
            <div class="hero-cta">
                {cta_buttons}
            </div>
        </div>
        <div class="hero-image">
            {hero_image}
        </div>
    </div>
</section>
""",
        "css": """
.hero {
    padding: 4rem 0;
    min-height: 80vh;
    display: flex;
    align-items: center;
    background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-primary) 100%);
}

.hero-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
}

.hero-title {
    font-size: 3.5rem;
    font-weight: bold;
    color: var(--text-primary);
    margin-bottom: 1rem;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: 1.25rem;
    color: var(--text-secondary);
    margin-bottom: 2rem;
    line-height: 1.6;
}

.hero-cta {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.hero-image {
    display: flex;
    justify-content: center;
    align-items: center;
}

.hero-image img {
    max-width: 100%;
    height: auto;
    border-radius: 12px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

@media (max-width: 968px) {
    .hero-container {
        grid-template-columns: 1fr;
        text-align: center;
    }
    
    .hero-title {
        font-size: 2.5rem;
    }
    
    .hero-cta {
        justify-content: center;
    }
}
"""
    },
    
    "features": {
        "modern": """
<section class="features">
    <div class="features-container">
        <h2 class="section-title">{section_title}</h2>
        <p class="section-subtitle">{section_subtitle}</p>
        <div class="features-grid">
            {feature_items}
        </div>
    </div>
</section>
""",
        "css": """
.features {
    padding: 6rem 0;
    background: var(--bg-primary);
}

.features-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.section-title {
    font-size: 2.5rem;
    font-weight: bold;
    text-align: center;
    color: var(--text-primary);
    margin-bottom: 1rem;
}

.section-subtitle {
    font-size: 1.125rem;
    text-align: center;
    color: var(--text-secondary);
    margin-bottom: 3rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.feature-card {
    padding: 2rem;
    background: var(--bg-secondary);
    border-radius: 12px;
    transition: transform 0.3s, box-shadow 0.3s;
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.feature-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.feature-card h3 {
    font-size: 1.5rem;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
}

.feature-card p {
    color: var(--text-secondary);
    line-height: 1.6;
}
"""
    },
    
    "gallery": {
        "modern": """
<section class="gallery">
    <div class="gallery-container">
        <h2 class="section-title">{section_title}</h2>
        <div class="gallery-grid">
            {gallery_items}
        </div>
    </div>
</section>
""",
        "css": """
.gallery {
    padding: 6rem 0;
    background: var(--bg-secondary);
}

.gallery-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}

.gallery-item {
    position: relative;
    overflow: hidden;
    border-radius: 12px;
    aspect-ratio: 4/3;
    cursor: pointer;
}

.gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s;
}

.gallery-item:hover img {
    transform: scale(1.1);
}

.gallery-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.7), transparent);
    padding: 1.5rem;
    transform: translateY(100%);
    transition: transform 0.3s;
}

.gallery-item:hover .gallery-overlay {
    transform: translateY(0);
}

.gallery-overlay h3 {
    color: white;
    margin: 0;
    font-size: 1.25rem;
}
"""
    },
    
    "contact": {
        "modern": """
<section class="contact">
    <div class="contact-container">
        <h2 class="section-title">{section_title}</h2>
        <p class="section-subtitle">{section_subtitle}</p>
        <form class="contact-form" id="contactForm">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Send Message</button>
        </form>
    </div>
</section>
""",
        "css": """
.contact {
    padding: 6rem 0;
    background: var(--bg-primary);
}

.contact-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 0 2rem;
}

.contact-form {
    margin-top: 2rem;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    color: var(--text-primary);
    font-weight: 500;
    margin-bottom: 0.5rem;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid var(--border);
    border-radius: 8px;
    background: var(--bg-secondary);
    color: var(--text-primary);
    font-size: 1rem;
    transition: border-color 0.3s;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--accent);
}

.btn {
    padding: 0.75rem 2rem;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
}

.btn-primary {
    background: var(--accent);
    color: white;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}
"""
    },
    
    "footer": {
        "modern": """
<footer class="footer">
    <div class="footer-container">
        <div class="footer-content">
            <div class="footer-brand">
                <h3>{brand_name}</h3>
                <p>{brand_description}</p>
            </div>
            <div class="footer-links">
                {footer_sections}
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; {year} {brand_name}. All rights reserved.</p>
        </div>
    </div>
</footer>
""",
        "css": """
.footer {
    background: var(--bg-secondary);
    padding: 4rem 0 2rem;
    border-top: 1px solid var(--border);
}

.footer-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.footer-content {
    display: grid;
    grid-template-columns: 2fr 3fr;
    gap: 4rem;
    margin-bottom: 3rem;
}

.footer-brand h3 {
    color: var(--text-primary);
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.footer-brand p {
    color: var(--text-secondary);
    line-height: 1.6;
}

.footer-links {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 2rem;
}

.footer-section h4 {
    color: var(--text-primary);
    margin-bottom: 1rem;
}

.footer-section ul {
    list-style: none;
    padding: 0;
}

.footer-section ul li {
    margin-bottom: 0.5rem;
}

.footer-section ul li a {
    color: var(--text-secondary);
    text-decoration: none;
    transition: color 0.3s;
}

.footer-section ul li a:hover {
    color: var(--accent);
}

.footer-bottom {
    text-align: center;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
    color: var(--text-secondary);
}

@media (max-width: 768px) {
    .footer-content {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
}
"""
    }
}

# JavaScript utilities for all components
COMMON_JS = """
// Mobile navigation toggle
document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
    }
    
    // Contact form handling
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Thank you for your message! This is a demo form.');
            contactForm.reset();
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
"""
