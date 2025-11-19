"use client";

import { useState } from "react";
import { useChat, ChatMessage } from "@/lib/useChat";

interface ChatInterfaceProps {
  sessionId: string;
}

export default function ChatInterface({ sessionId }: ChatInterfaceProps) {
  const { messages, sendMessage, connected } = useChat(sessionId);
  const [input, setInput] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (input.trim()) {
      sendMessage(input);
      setInput("");
    }
  };

  return (
    <div className="flex h-[600px] flex-col rounded-lg border bg-white shadow-sm">
      <div className="flex items-center justify-between border-b bg-gray-50 p-4">
        <h3 className="font-semibold text-gray-700">Creative Assistant</h3>
        <div
          className={`rounded-full px-2 py-1 text-xs ${connected ? "bg-green-100 text-green-800" : "bg-red-100 text-red-800"}`}
        >
          {connected ? "Connected" : "Disconnected"}
        </div>
      </div>

      <div className="flex-1 space-y-4 overflow-y-auto p-4">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`flex ${msg.sender === "USER" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-[80%] rounded-lg p-3 ${
                msg.sender === "USER"
                  ? "rounded-br-none bg-blue-600 text-white"
                  : msg.sender === "SYSTEM"
                    ? "w-full bg-gray-100 text-center text-xs text-gray-500"
                    : "rounded-bl-none bg-gray-100 text-gray-800"
              }`}
            >
              {msg.sender !== "USER" && msg.sender !== "SYSTEM" && (
                <div className="mb-1 text-xs font-bold text-gray-500">
                  {msg.sender}
                </div>
              )}
              {msg.content}
            </div>
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="border-t p-4">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type a message..."
            className="flex-1 rounded-md border px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
            disabled={!connected}
          />
          <button
            type="submit"
            disabled={!connected || !input.trim()}
            className="rounded-md bg-blue-600 px-4 py-2 text-white transition hover:bg-blue-700 disabled:opacity-50"
          >
            Send
          </button>
        </div>
      </form>
    </div>
  );
}
