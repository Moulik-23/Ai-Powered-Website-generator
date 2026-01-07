'use client';

import { useState, useEffect } from 'react';
import { getProjects, deleteProject, Project } from '@/lib/api';
import { formatDate } from '@/lib/utils';
import { FiTrash2, FiEye, FiClock } from 'react-icons/fi';

interface ProjectsListProps {
  onLoadProject: (project: Project) => void;
}

export default function ProjectsList({ onLoadProject }: ProjectsListProps) {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadProjects();
  }, []);

  const loadProjects = async () => {
    setLoading(true);
    setError('');
    try {
      const data = await getProjects();
      setProjects(data);
    } catch (err: any) {
      setError('Failed to load projects');
      console.error('Error loading projects:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id: string) => {
    if (!confirm('Are you sure you want to delete this project?')) {
      return;
    }

    try {
      await deleteProject(id);
      setProjects(projects.filter(p => p.id !== id));
    } catch (err) {
      alert('Failed to delete project');
      console.error('Error deleting project:', err);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-center py-12">
        <p className="text-red-600">{error}</p>
        <button
          onClick={loadProjects}
          className="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
        >
          Retry
        </button>
      </div>
    );
  }

  if (projects.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gray-100 mb-4">
          <FiClock className="w-8 h-8 text-gray-400" />
        </div>
        <h3 className="text-lg font-medium text-gray-900 mb-2">
          No saved projects yet
        </h3>
        <p className="text-gray-500">
          Generate and save websites to see them here
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-900">
          Saved Projects ({projects.length})
        </h3>
        <button
          onClick={loadProjects}
          className="text-sm text-blue-600 hover:text-blue-800"
        >
          Refresh
        </button>
      </div>

      <div className="space-y-3">
        {projects.map((project) => (
          <div
            key={project.id}
            className="bg-white border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow"
          >
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <h4 className="font-medium text-gray-900 mb-1">{project.name}</h4>
                <p className="text-sm text-gray-600 mb-2 line-clamp-2">
                  {project.prompt}
                </p>
                <div className="flex items-center space-x-4 text-xs text-gray-500">
                  <span className="flex items-center space-x-1">
                    <FiClock className="w-3 h-3" />
                    <span>{project.created_at ? formatDate(project.created_at) : 'Unknown'}</span>
                  </span>
                  <span className="px-2 py-1 bg-gray-100 rounded-full">
                    {project.color_scheme}
                  </span>
                  <span>{project.components.length} components</span>
                </div>
              </div>

              <div className="flex items-center space-x-2 ml-4">
                <button
                  onClick={() => onLoadProject(project)}
                  className="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
                  title="Load Project"
                >
                  <FiEye className="w-5 h-5" />
                </button>
                <button
                  onClick={() => project.id && handleDelete(project.id)}
                  className="p-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors"
                  title="Delete Project"
                >
                  <FiTrash2 className="w-5 h-5" />
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
