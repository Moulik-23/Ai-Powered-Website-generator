export const downloadFile = (content: string, filename: string, mimeType: string) => {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
};

export const downloadWebsite = (html: string, css: string, js: string) => {
  // Create a complete HTML file with embedded CSS and JS
  const completeHTML = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Website</title>
    <style>
${css}
    </style>
</head>
<body>
${html.replace(/<head>[\s\S]*?<\/head>/i, '').replace(/<\/?(!DOCTYPE |html|body)[^>]*>/gi, '')}
    <script>
${js}
    </script>
</body>
</html>`;

  downloadFile(completeHTML, 'index.html', 'text/html');
  
  // Also download separate files
  downloadFile(css, 'styles.css', 'text/css');
  downloadFile(js, 'script.js', 'text/javascript');
};

export const copyToClipboard = async (text: string) => {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (err) {
    console.error('Failed to copy:', err);
    return false;
  }
};

export const formatDate = (dateString: string) => {
  const date = new Date(dateString);
  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  }).format(date);
};
