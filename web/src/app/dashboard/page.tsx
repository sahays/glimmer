"use client";

import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api";
import Link from "next/link";

interface Project {
  project_id: number;
  project_name: string;
  owner_id: number;
  created_at: string;
}

async function fetchProjects() {
  const res = await api.get<Project[]>("/projects/");
  return res.data;
}

export default function DashboardPage() {
  const {
    data: projects,
    isLoading,
    isError,
  } = useQuery({
    queryKey: ["projects"],
    queryFn: fetchProjects,
  });

  if (isLoading) {
    return <div className="p-8">Loading projects...</div>;
  }

  if (isError) {
    return (
      <div className="p-8 text-red-500">
        Error loading projects. Is the API running?
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="mx-auto max-w-5xl">
        <header className="mb-8 flex items-center justify-between">
          <h1 className="text-3xl font-bold text-gray-900">Glimmer Projects</h1>
          <button className="rounded-md bg-black px-4 py-2 text-white transition hover:bg-gray-800">
            + New Project
          </button>
        </header>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
          {projects?.map((project) => (
            <Link
              key={project.project_id}
              href={`/project/${project.project_id}`}
              className="block rounded-lg border border-gray-200 bg-white p-6 shadow-sm transition hover:shadow-md"
            >
              <h2 className="mb-2 text-xl font-semibold text-gray-800">
                {project.project_name}
              </h2>
              <div className="text-sm text-gray-500">
                Created: {new Date(project.created_at).toLocaleDateString()}
              </div>
              <div className="mt-4 text-xs text-gray-400">
                ID: {project.project_id}
              </div>
            </Link>
          ))}

          {projects?.length === 0 && (
            <div className="col-span-full py-12 text-center text-gray-500">
              No projects found. Create one to get started!
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
