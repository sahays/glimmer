import { redirect } from "next/navigation";

export default function Home() {
  // Redirect root to dashboard for now
  redirect("/dashboard");
}
