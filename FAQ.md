# Frequently Asked Questions (FAQ)

## General Questions

### What is the AI Website Generator?
An AI-powered tool that creates complete, functional websites from natural language descriptions. Simply describe what you want, and the AI generates HTML, CSS, and JavaScript code.

### Do I need coding knowledge to use it?
No! The tool is designed for anyone. Just describe your website in plain English, and the AI handles all the technical details.

### How long does it take to generate a website?
Generation typically takes 10-30 seconds, depending on complexity and AI response time.

### Can I customize the generated websites?
Yes! You can:
- Download the code and edit manually
- Try different color schemes
- Regenerate with modified prompts
- Customize templates in the source code

## Technical Questions

### Which AI model does it use?
Google Gemini Pro by default. The architecture supports adding other models like Claude or Llama.

### What browsers are supported?
All modern browsers:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Does it work offline?
No, it requires internet connection for:
- AI API calls (Gemini)
- Database operations (if using cloud MongoDB)

### Can I use it commercially?
Yes! The MIT license allows commercial use. However, check Google Gemini API terms for any restrictions on AI-generated content.

## Setup & Installation

### I'm getting "Python not found" error
Make sure Python 3.9+ is installed and added to your system PATH. Download from [python.org](https://python.org).

### MongoDB connection fails
Common solutions:
- Ensure MongoDB service is running
- Check connection string in `.env`
- For MongoDB Atlas, verify IP whitelist
- Check firewall settings

### "GEMINI_API_KEY not found" error
1. Create a `.env` file in the `backend` directory
2. Add: `GEMINI_API_KEY=your_actual_key_here`
3. Get a key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Frontend won't start
1. Check Node.js version: `node --version` (need 18+)
2. Delete `node_modules` and `.next` folders
3. Run `npm install` again
4. Check if port 3000 is available

### Backend shows import errors
1. Ensure virtual environment is activated
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check Python version: `python --version`

## Usage Questions

### What makes a good prompt?
Good prompts are:
- **Specific**: "Portfolio for wedding photographer" not just "portfolio"
- **Detailed**: Mention sections you want (hero, gallery, contact)
- **Clear**: Describe the purpose and audience
- See [EXAMPLE_PROMPTS.md](EXAMPLE_PROMPTS.md) for examples

### Can I save generated websites?
Yes! Click the "Save" button in the preview tab to save projects to the database. You can load them later from the Projects tab.

### How do I download the website?
Click the "Download" button in the preview tab. You'll get three files:
- `index.html` - Complete webpage
- `styles.css` - Stylesheet
- `script.js` - JavaScript

### Can I edit the code after generation?
Yes! View the code in the "Code" tab, copy it, and edit in your favorite editor. Or download and modify the files.

### Why does my website look different than expected?
- Try rewording your prompt more specifically
- Use the advanced options to change color schemes
- Regenerate with additional details
- Check the example prompts for ideas

## Feature Questions

### What components are available?
Currently includes:
- Navigation (responsive menu)
- Hero (header section)
- Features (grid layout)
- Gallery (image grid)
- Contact (form)
- Footer (multi-column)

More can be added - see [CUSTOMIZATION.md](CUSTOMIZATION.md).

### What color schemes are available?
Seven built-in schemes:
1. Default Light
2. Dark Mode
3. Ocean Blue
4. Sunset Orange
5. Forest Green
6. Royal Purple
7. Minimal Gray

### Are the websites responsive?
Yes! All generated websites are fully responsive and work on:
- Desktop (1200px+)
- Tablet (768px - 1199px)
- Mobile (< 768px)

Preview them using the device buttons in the preview tab.

### Can I add my own images?
The generator uses placeholder images. After downloading, replace image URLs with your own in the HTML file.

### Does it generate content?
Yes! The AI generates:
- Page titles
- Headlines and subtitles
- Feature descriptions
- Navigation labels
- Meta descriptions
- Button text

## API & Development

### Can I use the API programmatically?
Yes! The backend provides a RESTful API. See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for endpoints and examples.

### How do I add custom components?
1. Edit `backend/app/templates/components.py`
2. Add your component HTML, CSS, and JS
3. Update AI prompts to recognize it
4. See [CUSTOMIZATION.md](CUSTOMIZATION.md) for details

### Can I integrate other AI models?
Yes! Create a new service class implementing the same interface as `AIService`. See customization guide for examples.

### Is there rate limiting?
Not by default. For production, implement rate limiting using slowapi or similar. See [DEPLOYMENT.md](DEPLOYMENT.md).

### Can I contribute to the project?
Absolutely! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Contributions welcome!

## Database Questions

### What database is required?
MongoDB (local or cloud). MongoDB Atlas offers a free tier perfect for testing.

### How much data does it store?
For each saved project:
- HTML (~5-20 KB)
- CSS (~5-15 KB)
- JavaScript (~1-5 KB)
- Metadata (~1 KB)

Total: ~12-41 KB per project

### Can I use a different database?
Yes, but requires code changes. The architecture uses Motor (async MongoDB). You'd need to:
1. Update `models/database.py`
2. Modify CRUD operations in `routes/projects.py`
3. Update schemas if needed

### How do I backup the database?
For MongoDB:
```bash
mongodump --out /path/to/backup
```
See [DEPLOYMENT.md](DEPLOYMENT.md) for automated backup scripts.

## Performance Questions

### Why is generation slow?
Generation time depends on:
- AI API response time (10-20s typical)
- Internet connection speed
- Prompt complexity
- Server load

### Can it handle multiple users?
Yes, FastAPI is async and handles concurrent requests. For high traffic:
- Use load balancing
- Scale horizontally
- Implement caching
- See [DEPLOYMENT.md](DEPLOYMENT.md) for scaling strategies

### How many websites can I generate?
Unlimited locally. For production, consider:
- Gemini API rate limits and quotas
- Database storage capacity
- Server resources

### Can I cache AI responses?
Yes! Implement caching in `ai_service.py` to save common patterns. Requires Redis or similar.

## Pricing & Costs

### Is it free to use?
The code is free (MIT license). However, you need:
- Google Gemini API key (free tier available, then pay-per-use)
- MongoDB (free tier available)
- Hosting costs if deploying online

### How much does Gemini API cost?
Check current pricing at [Google AI Pricing](https://ai.google.dev/pricing). Free tier includes generous limits for testing.

### Are there hidden costs?
Potential costs:
- Gemini API usage beyond free tier
- Cloud hosting (if not self-hosting)
- Domain name (if wanted)
- SSL certificate (free with Let's Encrypt)
- MongoDB Atlas beyond free tier

## Security Questions

### Is it secure?
Basic security implemented:
- Environment variables for secrets
- Input validation
- CORS configuration
- Parameterized queries

For production, add:
- Authentication
- Rate limiting
- HTTPS
- See [DEPLOYMENT.md](DEPLOYMENT.md) security checklist

### Can users execute malicious code?
Generated code runs in sandboxed iframe with `sandbox` attribute. However, always validate and review AI-generated code before production use.

### How is my API key protected?
- Stored in `.env` file (not committed to git)
- Used server-side only
- Never exposed to frontend

### Should I add authentication?
For public deployment: YES! Add user authentication to:
- Prevent API abuse
- Track user projects
- Manage quotas
- See customization guide for implementation

## Deployment Questions

### Can I deploy this online?
Yes! Multiple options:
- Traditional server (Ubuntu, Windows Server)
- Docker containers
- Vercel (frontend) + Railway/Render (backend)
- AWS, Google Cloud, Azure

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed guides.

### What hosting is recommended?
**Frontend:**
- Vercel (easiest, free tier)
- Netlify
- AWS S3 + CloudFront

**Backend:**
- Railway
- Render
- DigitalOcean
- AWS EC2

### Do I need a domain name?
No, but recommended for production. Can use:
- Provider's default URLs for testing
- Custom domain for professional use

### How do I set up HTTPS?
Use Let's Encrypt (free):
```bash
sudo certbot --nginx -d yourdomain.com
```
See deployment guide for full instructions.

## Troubleshooting

### Generation returns error
Check:
1. GEMINI_API_KEY is valid
2. API has available quota
3. Internet connection works
4. Backend logs for details

### Preview doesn't load
- Check browser console for errors
- Verify backend is running
- Check API_URL in frontend `.env.local`
- Try regenerating the website

### Downloaded files don't work
- Ensure all three files (HTML, CSS, JS) are in same folder
- Check browser console for errors
- Verify HTML file opens in browser
- Check image URLs are accessible

### Projects won't save
- Verify MongoDB is running
- Check database connection string
- Ensure backend can reach database
- Check backend logs for errors

## Still Have Questions?

- 📖 Check our [documentation](README.md)
- 🐛 Open an [issue on GitHub](https://github.com/yourusername/ai-website-generator/issues)
- 💬 Start a [discussion](https://github.com/yourusername/ai-website-generator/discussions)
- 📧 Contact support (if applicable)

---

Can't find your answer? Open an issue and we'll add it to this FAQ!
