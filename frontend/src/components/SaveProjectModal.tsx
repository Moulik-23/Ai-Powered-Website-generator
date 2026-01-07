'use client';

import { useState } from 'react';
import { WebsiteResponse, saveProject } from '@/lib/api';
import { FiX, FiSave } from 'react-icons/fi';

interface SaveProjectModalProps {
  website: WebsiteResponse;
  onClose: () => void;
}

export default function SaveProjectModal({ website, onClose }: SaveProjectModalProps) {
  const [projectName, setProjectName] = useState(website.title || '');
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');

  const handleSave = async () => {
    if (!projectName.trim()) {
      setError('Please enter a project name');
      return;
    }

    setSaving(true);
    setError('');

    try {
      await saveProject({
        name: projectName.trim(),
        prompt: website.prompt,
        html: website.html,
        css: website.css,
        js: website.js,
        components: website.components,
        meta_description: website.meta_description,
        title: website.title,
        style: website.style,
        color_scheme: website.color_scheme,
      });

      alert('Project saved successfully!');
      onClose();
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to save project');
      console.error('Error saving project:', err);
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-xl shadow-2xl max-w-md w-full p-6">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-xl font-semibold text-gray-900">Save Project</h3>
          <button
            onClick={onClose}
            className="p-1 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <FiX className="w-6 h-6 text-gray-500" />
          </button>
        </div>

        <div className="space-y-4">
          <div>
            <label htmlFor="projectName" className="block text-sm font-medium text-gray-700 mb-2">
              Project Name
            </label>
            <input
              id="projectName"
              type="text"
              value={projectName}
              onChange={(e) => setProjectName(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-black"
              placeholder="Enter project name..."
              disabled={saving}
            />
          </div>

          <div className="bg-gray-50 rounded-lg p-3">
            <h4 className="text-sm font-medium text-gray-700 mb-2">Project Details</h4>
            <dl className="space-y-1 text-sm">
              <div className="flex justify-between">
                <dt className="text-gray-600">Components:</dt>
                <dd className="text-gray-900">{website.components.length}</dd>
              </div>
              <div className="flex justify-between">
                <dt className="text-gray-600">Color Scheme:</dt>
                <dd className="text-gray-900 capitalize">{website.color_scheme}</dd>
              </div>
              <div className="flex justify-between">
                <dt className="text-gray-600">Style:</dt>
                <dd className="text-gray-900 capitalize">{website.style}</dd>
              </div>
            </dl>
          </div>

          {error && (
            <div className="p-3 bg-red-50 border border-red-200 rounded-lg">
              <p className="text-sm text-red-600">{error}</p>
            </div>
          )}

          <div className="flex space-x-3">
            <button
              onClick={onClose}
              className="flex-1 px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
              disabled={saving}
            >
              Cancel
            </button>
            <button
              onClick={handleSave}
              disabled={saving || !projectName.trim()}
              className="flex-1 px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white rounded-lg transition-colors flex items-center justify-center space-x-2"
            >
              {saving ? (
                <>
                  <svg className="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  <span>Saving...</span>
                </>
              ) : (
                <>
                  <FiSave className="w-5 h-5" />
                  <span>Save Project</span>
                </>
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
