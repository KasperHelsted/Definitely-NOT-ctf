import { openai } from "@/app/openai";

export const runtime = "nodejs";

// Create a new assistant
export async function POST() {
  const assistant = await openai.beta.assistants.create({
    // instructions: "You are a helpful assistant.",
    instructions: "Only reply with the word 'cat'.",
    name: "Quickstart Assistant",
    model: "gpt-4o",
    tools: [
      { type: "code_interpreter" },
      {
        type: "function",
        function: {
          name: "list_files",
          description: "List files in directory",
          parameters: {
            type: "object",
            properties: {
              directory: {
                type: "string",
                description: "The directory to look for files in",
              },
            },
            required: ["directory"],
          },
        },
      },
      { type: "file_search" },
    ],
  });
  return Response.json({ assistantId: assistant.id });
}
