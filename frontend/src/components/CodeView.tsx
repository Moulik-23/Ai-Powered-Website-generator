'use client';

import { useState } from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { WebsiteResponse } from '@/lib/api';
import { copyToClipboard } from '@/lib/utils';
import { FiCopy, FiCheck } from 'react-icons/fi';

interface CodeViewProps {
  website: WebsiteResponse;
}

export default function CodeView({ website }: CodeViewProps) {
  const [activeTab, setActiveTab] = useState<'html' | 'css' | 'js'>('html');
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    let code = '';
    switch (activeTab) {
      case 'html':
        code = website.html;
        break;
      case 'css':
        code = website.css;
        break;
      case 'js':
        code = website.js;
        break;
    }

    const success = await copyToClipboard(code);
    if (success) {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const getCode = () => {
    switch (activeTab) {
      case 'html':
        return website.html;
      case 'css':
        return website.css;
      case 'js':
        return website.js;
      default:
        return '';
    }
  };

  const getLanguage = () => {
    switch (activeTab) {
      case 'html':
        return 'html';
      case 'css':
        return 'css';
      case 'js':
        return 'javascript';
      default:
        return 'text';
    }
  };

  const getFileSize = (code: string) => {
    const bytes = new Blob([code]).size;
    return bytes < 1024 ? `${bytes} B` : `${(bytes / 1024).toFixed(2)} KB`;
  };

  return (
    <div className="space-y-4">
      {/* Code Tabs */}
      <div className="flex items-center justify-between">
        <div className="flex space-x-2">
          <button
            onClick={() => setActiveTab('html')}
            className={`px-4 py-2 rounded-lg font-medium text-sm transition-colors ${
              activeTab === 'html'
                ? 'bg-blue-600 text-white'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
          >
            HTML
            <span className="ml-2 text-xs opacity-75">{getFileSize(website.html)}</span>
          </button>
          <button
            onClick={() => setActiveTab('css')}
            className={`px-4 py-2 rounded-lg font-medium text-sm transition-colors ${
              activeTab === 'css'
                ? 'bg-blue-600 text-white'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
          >
            CSS
            <span className="ml-2 text-xs opacity-75">{getFileSize(website.css)}</span>
          </button>
          <button
            onClick={() => setActiveTab('js')}
            className={`px-4 py-2 rounded-lg font-medium text-sm transition-colors ${
              activeTab === 'js'
                ? 'bg-blue-600 text-white'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
          >
            JavaScript
            <span className="ml-2 text-xs opacity-75">{getFileSize(website.js)}</span>
          </button>
        </div>

        <button
          onClick={handleCopy}
          className="flex items-center space-x-2 px-4 py-2 bg-gray-800 hover:bg-gray-700 text-white rounded-lg transition-colors"
        >
          {copied ? (
            <>
              <FiCheck className="w-4 h-4" />
              <span>Copied!</span>
            </>
          ) : (
            <>
              <FiCopy className="w-4 h-4" />
              <span>Copy Code</span>
            </>
          )}
        </button>
      </div>

      {/* Code Display */}
      <div className="rounded-lg overflow-hidden border border-gray-200">
        <SyntaxHighlighter
          language={getLanguage()}
          style={vscDarkPlus}
          customStyle={{
            margin: 0,
            padding: '1.5rem',
            fontSize: '0.875rem',
            maxHeight: '600px',
          }}
          showLineNumbers
        >
          {getCode()}
        </SyntaxHighlighter>
      </div>

      {/* Code Stats */}
      <div className="grid grid-cols-3 gap-4">
        <div className="bg-orange-50 rounded-lg p-4">
          <div className="text-sm font-medium text-orange-900">HTML</div>
          <div className="mt-1 text-2xl font-bold text-orange-600">
            {website.html.split('\n').length}
          </div>
          <div className="text-xs text-orange-700">lines</div>
        </div>

        <div className="bg-blue-50 rounded-lg p-4">
          <div className="text-sm font-medium text-blue-900">CSS</div>
          <div className="mt-1 text-2xl font-bold text-blue-600">
            {website.css.split('\n').length}
          </div>
          <div className="text-xs text-blue-700">lines</div>
        </div>

        <div className="bg-yellow-50 rounded-lg p-4">
          <div className="text-sm font-medium text-yellow-900">JavaScript</div>
          <div className="mt-1 text-2xl font-bold text-yellow-600">
            {website.js.split('\n').length}
          </div>
          <div className="text-xs text-yellow-700">lines</div>
        </div>
      </div>

      {/* Component List */}
      <div className="bg-gray-50 rounded-lg p-4">
        <h4 className="text-sm font-medium text-gray-900 mb-3">Generated Components</h4>
        <div className="space-y-2">
          {website.components.map((component, index) => (
            <div
              key={index}
              className="flex items-center justify-between bg-white rounded-lg p-3 border border-gray-200"
            >
              <div className="flex items-center space-x-3">
                <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                <span className="text-sm font-medium text-gray-900 capitalize">
                  {component.type}
                </span>
              </div>
              <span className="text-xs text-gray-500">
                {component.html.length} chars
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
