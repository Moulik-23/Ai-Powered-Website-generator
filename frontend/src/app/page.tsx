'use client';

import { useState } from 'react';
import GeneratorForm from '@/components/GeneratorForm';
import WebsitePreview from '@/components/WebsitePreview';
import CodeView from '@/components/CodeView';
import ProjectsList from '@/components/ProjectsList';
import { WebsiteResponse } from '@/lib/api';
import { FiCode, FiEye, FiFolder } from 'react-icons/fi';

export default function Home() {
  const [generatedWebsite, setGeneratedWebsite] = useState<WebsiteResponse | null>(null);
  const [isGenerating, setIsGenerating] = useState(false);
  const [activeTab, setActiveTab] = useState<'preview' | 'code' | 'projects'>('preview');

  const handleGenerate = (website: WebsiteResponse) => {
    setGeneratedWebsite(website);
    setActiveTab('preview');
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">
                🤖 AI Website Generator
              </h1>
              <p className="mt-1 text-sm text-gray-500">
                Transform your ideas into beautiful websites with AI
              </p>
            </div>
            <div className="flex items-center space-x-2 text-sm text-gray-600">
              <span className="px-3 py-1 bg-green-100 text-green-800 rounded-full">
                Powered by Gemini
              </span>
            </div>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Left Column - Generator Form */}
          <div className="lg:col-span-1">
            <div className="bg-white rounded-xl shadow-lg p-6 sticky top-8">
              <GeneratorForm
                onGenerate={handleGenerate}
                isGenerating={isGenerating}
                setIsGenerating={setIsGenerating}
              />
            </div>
          </div>

          {/* Right Column - Preview/Code/Projects */}
          <div className="lg:col-span-2">
            {/* Tabs */}
            <div className="bg-white rounded-t-xl shadow-lg">
              <div className="border-b border-gray-200">
                <nav className="flex space-x-8 px-6" aria-label="Tabs">
                  <button
                    onClick={() => setActiveTab('preview')}
                    className={`py-4 px-1 border-b-2 font-medium text-sm flex items-center space-x-2 ${
                      activeTab === 'preview'
                        ? 'border-blue-500 text-blue-600'
                        : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                    }`}
                  >
                    <FiEye className="w-5 h-5" />
                    <span>Preview</span>
                  </button>
                  <button
                    onClick={() => setActiveTab('code')}
                    className={`py-4 px-1 border-b-2 font-medium text-sm flex items-center space-x-2 ${
                      activeTab === 'code'
                        ? 'border-blue-500 text-blue-600'
                        : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                    }`}
                    disabled={!generatedWebsite}
                  >
                    <FiCode className="w-5 h-5" />
                    <span>Code</span>
                  </button>
                  <button
                    onClick={() => setActiveTab('projects')}
                    className={`py-4 px-1 border-b-2 font-medium text-sm flex items-center space-x-2 ${
                      activeTab === 'projects'
                        ? 'border-blue-500 text-blue-600'
                        : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                    }`}
                  >
                    <FiFolder className="w-5 h-5" />
                    <span>Projects</span>
                  </button>
                </nav>
              </div>

              {/* Tab Content */}
              <div className="p-6">
                {activeTab === 'preview' && (
                  generatedWebsite ? (
                    <WebsitePreview website={generatedWebsite} />
                  ) : (
                    <div className="text-center py-12">
                      <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-blue-100 mb-4">
                        <FiEye className="w-8 h-8 text-blue-600" />
                      </div>
                      <h3 className="text-lg font-medium text-gray-900 mb-2">
                        No website generated yet
                      </h3>
                      <p className="text-gray-500">
                        Enter a description and click Generate to see your website
                      </p>
                    </div>
                  )
                )}

                {activeTab === 'code' && (
                  generatedWebsite ? (
                    <CodeView website={generatedWebsite} />
                  ) : (
                    <div className="text-center py-12">
                      <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-blue-100 mb-4">
                        <FiCode className="w-8 h-8 text-blue-600" />
                      </div>
                      <h3 className="text-lg font-medium text-gray-900 mb-2">
                        No code to display
                      </h3>
                      <p className="text-gray-500">
                        Generate a website first to view the code
                      </p>
                    </div>
                  )
                )}

                {activeTab === 'projects' && (
                  <ProjectsList onLoadProject={(project) => {
                    setGeneratedWebsite(project as WebsiteResponse);
                    setActiveTab('preview');
                  }} />
                )}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="mt-16 bg-white border-t border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <p className="text-center text-gray-500 text-sm">
            © 2026 AI Website Generator. Built with Next.js, FastAPI & Google Gemini
          </p>
        </div>
      </footer>
    </main>
  );
}
