'use client';

import { useState, useEffect } from 'react';
import { generateWebsite, getColorSchemes, WebsiteResponse } from '@/lib/api';
import { FiZap, FiSettings } from 'react-icons/fi';

interface GeneratorFormProps {
  onGenerate: (website: WebsiteResponse) => void;
  isGenerating: boolean;
  setIsGenerating: (value: boolean) => void;
}

export default function GeneratorForm({ onGenerate, isGenerating, setIsGenerating }: GeneratorFormProps) {
  const [prompt, setPrompt] = useState('');
  const [style, setStyle] = useState('modern');
  const [colorScheme, setColorScheme] = useState('default');
  const [colorSchemes, setColorSchemes] = useState<any[]>([]);
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    loadColorSchemes();
  }, []);

  const loadColorSchemes = async () => {
    try {
      const schemes = await getColorSchemes();
      setColorSchemes(schemes);
    } catch (err) {
      console.error('Error loading color schemes:', err);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!prompt.trim()) {
      setError('Please enter a website description');
      return;
    }

    setError('');
    setIsGenerating(true);

    try {
      const result = await generateWebsite({
        prompt: prompt.trim(),
        style,
        color_scheme: colorScheme,
      });

      onGenerate(result);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to generate website. Please try again.');
      console.error('Generation error:', err);
    } finally {
      setIsGenerating(false);
    }
  };

  const examples = [
    'Create a portfolio website for a photographer',
    'Build a modern landing page for a SaaS startup',
    'Design a restaurant website with menu and contact form',
    'Make a personal blog for a travel writer',
  ];

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div>
        <label htmlFor="prompt" className="block text-sm font-medium text-gray-700 mb-2">
          Describe Your Website
        </label>
        <textarea
          id="prompt"
          rows={6}
          className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none text-black"
          placeholder="E.g., Create a modern portfolio website for a graphic designer with a gallery, about section, and contact form..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          disabled={isGenerating}
        />
        <p className="mt-2 text-xs text-gray-500">
          Be specific about the type of website, content sections, and style preferences
        </p>
      </div>

      {/* Example Prompts */}
      <div>
        <p className="text-xs font-medium text-gray-700 mb-2">Examples:</p>
        <div className="space-y-1">
          {examples.map((example, index) => (
            <button
              key={index}
              type="button"
              onClick={() => setPrompt(example)}
              className="block w-full text-left text-xs text-blue-600 hover:text-blue-800 hover:bg-blue-50 px-2 py-1 rounded"
              disabled={isGenerating}
            >
              → {example}
            </button>
          ))}
        </div>
      </div>

      {/* Advanced Options */}
      <div>
        <button
          type="button"
          onClick={() => setShowAdvanced(!showAdvanced)}
          className="flex items-center space-x-2 text-sm font-medium text-gray-700 hover:text-gray-900"
        >
          <FiSettings className="w-4 h-4" />
          <span>Advanced Options</span>
          <span className="text-gray-400">
            {showAdvanced ? '▼' : '▶'}
          </span>
        </button>

        {showAdvanced && (
          <div className="mt-4 space-y-4 p-4 bg-gray-50 rounded-lg">
            <div>
              <label htmlFor="style" className="block text-sm font-medium text-gray-700 mb-2">
                Design Style
              </label>
              <select
                id="style"
                value={style}
                onChange={(e) => setStyle(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 text-black"
                disabled={isGenerating}
              >
                <option value="modern">Modern</option>
              </select>
            </div>

            <div>
              <label htmlFor="colorScheme" className="block text-sm font-medium text-gray-700 mb-2">
                Color Scheme
              </label>
              <select
                id="colorScheme"
                value={colorScheme}
                onChange={(e) => setColorScheme(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 text-black"
                disabled={isGenerating}
              >
                {colorSchemes.map((scheme) => (
                  <option key={scheme.id} value={scheme.id}>
                    {scheme.name}
                  </option>
                ))}
              </select>
            </div>
          </div>
        )}
      </div>

      {error && (
        <div className="p-3 bg-red-50 border border-red-200 rounded-lg">
          <p className="text-sm text-red-600">{error}</p>
        </div>
      )}

      <button
        type="submit"
        disabled={isGenerating || !prompt.trim()}
        className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed text-white font-medium py-3 px-6 rounded-lg transition-colors flex items-center justify-center space-x-2"
      >
        {isGenerating ? (
          <>
            <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span>Generating Website...</span>
          </>
        ) : (
          <>
            <FiZap className="w-5 h-5" />
            <span>Generate Website</span>
          </>
        )}
      </button>
    </form>
  );
}
