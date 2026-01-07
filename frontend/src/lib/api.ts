import axios from 'axios';

const API_URL = (process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000').replace(/\/$/, '');

export interface GenerateWebsiteRequest {
  prompt: string;
  style?: string;
  color_scheme?: string;
}

export interface WebsiteResponse {
  html: string;
  css: string;
  js: string;
  components: any[];
  meta_description: string;
  title: string;
  prompt: string;
  style: string;
  color_scheme: string;
}

export interface Project {
  id?: string;
  name: string;
  prompt: string;
  html: string;
  css: string;
  js: string;
  components: any[];
  meta_description: string;
  title: string;
  style: string;
  color_scheme: string;
  created_at?: string;
  updated_at?: string;
}

const api = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const generateWebsite = async (
  request: GenerateWebsiteRequest
): Promise<WebsiteResponse> => {
  const response = await api.post('/generate', request);
  return response.data;
};

export const getColorSchemes = async () => {
  const response = await api.get('/color-schemes');
  return response.data.color_schemes;
};

export const getStyles = async () => {
  const response = await api.get('/styles');
  return response.data.styles;
};

export const saveProject = async (project: Project) => {
  const response = await api.post('/projects', project);
  return response.data;
};

export const getProjects = async () => {
  const response = await api.get('/projects');
  return response.data.projects;
};

export const getProject = async (id: string) => {
  const response = await api.get(`/projects/${id}`);
  return response.data;
};

export const updateProject = async (id: string, project: Project) => {
  const response = await api.put(`/projects/${id}`, project);
  return response.data;
};

export const deleteProject = async (id: string) => {
  const response = await api.delete(`/projects/${id}`);
  return response.data;
};

export default api;
