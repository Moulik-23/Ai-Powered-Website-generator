'use client';

import { useState, useEffect } from 'react';
import { WebsiteResponse } from '@/lib/api';
import { downloadWebsite } from '@/lib/utils';
import { FiDownload, FiMaximize2, FiMonitor, FiTablet, FiSmartphone, FiSave } from 'react-icons/fi';
import SaveProjectModal from './SaveProjectModal';

interface WebsitePreviewProps {
  website: WebsiteResponse;
}

export default function WebsitePreview({ website }: WebsitePreviewProps) {
  const [iframeKey, setIframeKey] = useState(0);
  const [viewportSize, setViewportSize] = useState<'desktop' | 'tablet' | 'mobile'>('desktop');
  const [showSaveModal, setShowSaveModal] = useState(false);
  const [previewHTML, setPreviewHTML] = useState('');

  useEffect(() => {
    // Create complete HTML for preview
    const completeHTML = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${website.title}</title>
    <style>${website.css}</style>
</head>
<body>
${website.html.replace(/<head>[\s\S]*?<\/head>/i, '').replace(/<\/?(!DOCTYPE |html|body)[^>]*>/gi, '')}
    <script>${website.js}</script>
</body>
</html>`;

    setPreviewHTML(completeHTML);
    setIframeKey(prev => prev + 1);
  }, [website]);

  const handleDownload = () => {
    downloadWebsite(website.html, website.css, website.js);
  };

  const handleFullscreen = () => {
    const iframe = document.getElementById('preview-iframe') as HTMLIFrameElement;
    if (iframe?.requestFullscreen) {
      iframe.requestFullscreen();
    }
  };

  const getViewportWidth = () => {
    switch (viewportSize) {
      case 'mobile':
        return '375px';
      case 'tablet':
        return '768px';
      default:
        return '100%';
    }
  };

  return (
    <div className="space-y-4">
      {/* Toolbar */}
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <h3 className="text-lg font-semibold text-gray-900">{website.title}</h3>
          <span className="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full">
            {website.color_scheme}
          </span>
        </div>

        <div className="flex items-center space-x-2">
          {/* Viewport Toggles */}
          <div className="flex items-center space-x-1 bg-gray-100 rounded-lg p-1">
            <button
              onClick={() => setViewportSize('desktop')}
              className={`p-2 rounded text-black ${viewportSize === 'desktop' ? 'bg-white shadow-sm' : 'hover:bg-gray-200'}`}
              title="Desktop View"
            >
              <FiMonitor className="w-4 h-4" />
            </button>
            <button
              onClick={() => setViewportSize('tablet')}
              className={`p-2 rounded text-black ${viewportSize === 'tablet' ? 'bg-white shadow-sm' : 'hover:bg-gray-200'}`}
              title="Tablet View"
            >
              <FiTablet className="w-4 h-4" />
            </button>
            <button
              onClick={() => setViewportSize('mobile')}
              className={`p-2 rounded text-black ${viewportSize === 'mobile' ? 'bg-white shadow-sm' : 'hover:bg-gray-200'}`}
              title="Mobile View"
            >
              <FiSmartphone className="w-4 h-4" />
            </button>
          </div>

          <button
            onClick={handleFullscreen}
            className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
            title="Fullscreen"
          >
            <FiMaximize2 className="w-5 h-5 text-gray-600" />
          </button>

          <button
            onClick={() => setShowSaveModal(true)}
            className="flex items-center space-x-2 px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg transition-colors"
          >
            <FiSave className="w-4 h-4" />
            <span>Save</span>
          </button>

          <button
            onClick={handleDownload}
            className="flex items-center space-x-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors"
          >
            <FiDownload className="w-4 h-4" />
            <span>Download</span>
          </button>
        </div>
      </div>

      {/* Preview Frame */}
      <div className="bg-gray-100 rounded-lg p-4 flex justify-center">
        <div
          style={{
            width: getViewportWidth(),
            transition: 'width 0.3s ease',
          }}
          className="bg-white rounded-lg shadow-xl overflow-hidden"
        >
          <iframe
            key={iframeKey}
            id="preview-iframe"
            srcDoc={previewHTML}
            className="w-full border-0"
            style={{ height: '600px' }}
            title="Website Preview"
            sandbox="allow-scripts allow-same-origin"
          />
        </div>
      </div>

      {/* Metadata */}
      <div className="bg-gray-50 rounded-lg p-4">
        <h4 className="text-sm font-medium text-gray-700 mb-2">Website Information</h4>
        <dl className="space-y-2">
          <div className="flex">
            <dt className="text-sm text-gray-600 w-32">Title:</dt>
            <dd className="text-sm text-gray-900">{website.title}</dd>
          </div>
          <div className="flex">
            <dt className="text-sm text-gray-600 w-32">Description:</dt>
            <dd className="text-sm text-gray-900">{website.meta_description}</dd>
          </div>
          <div className="flex">
            <dt className="text-sm text-gray-600 w-32">Prompt:</dt>
            <dd className="text-sm text-gray-900 italic">&quot;{website.prompt}&quot;</dd>
          </div>
          <div className="flex">
            <dt className="text-sm text-gray-600 w-32">Components:</dt>
            <dd className="text-sm text-gray-900">{website.components.length} sections</dd>
          </div>
        </dl>
      </div>

      {showSaveModal && (
        <SaveProjectModal
          website={website}
          onClose={() => setShowSaveModal(false)}
        />
      )}
    </div>
  );
}
