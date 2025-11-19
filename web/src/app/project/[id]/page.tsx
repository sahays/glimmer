"use client";

import { useParams } from "next/navigation";
import ChatInterface from "@/components/ChatInterface";
import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";

interface Project {
  project_id: string; // UUID
  project_name: string;
  owner_id: string;
  created_at: string;
}

async function fetchProject(id: string) {
  const res = await api.get<Project>(`/projects/${id}`);
  return res.data;
}

export default function ProjectPage() {
  const params = useParams();
  const projectId = params.id as string;

  const { data: project, isLoading } = useQuery({
    queryKey: ["project", projectId],
    queryFn: () => fetchProject(projectId),
  });

  if (isLoading) return <div className="p-8">Loading project...</div>;
  if (!project) return <div className="p-8">Project not found</div>;

  // For now, use the projectId as the sessionId. In real app, we might create a Session entity.
  const sessionId = projectId;

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="mx-auto max-w-6xl">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">
            {project.project_name}
          </h1>
          <p className="text-sm text-gray-500">ID: {project.project_id}</p>
        </div>

        <div className="grid grid-cols-1 gap-8 lg:grid-cols-3">
          {/* Left: Asset Library (Placeholder) */}
          <div className="space-y-6 lg:col-span-1">
            <div className="h-full rounded-lg border bg-white p-6 shadow-sm">
              <h2 className="mb-4 text-lg font-semibold">Assets</h2>
              <div className="py-8 text-center text-sm text-gray-400">
                No assets yet.
              </div>
            </div>
          </div>

          {/* Right: Chat Interface */}
          <div className="lg:col-span-2">
            <ChatInterface sessionId={sessionId} />
          </div>
        </div>
      </div>
    </div>
  );
}
