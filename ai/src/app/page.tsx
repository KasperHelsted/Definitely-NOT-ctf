"use client";

import React, { useState } from "react";
import styles from "./page.module.css";
import Chat from "./components/chat";
import { listFiles } from "./utils/files";
import { RequiredActionFunctionToolCall } from "openai/resources/beta/threads/runs/runs";


const FunctionCalling = () => {
  const [lastResult, setLastResult] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | undefined>();
  
  const functionCallHandler = async (call: RequiredActionFunctionToolCall) => {
    if (call?.function?.name !== "list_files") return;

    try {
      const args = JSON.parse(call.function.arguments);
      
      // Direct call to the server action
      const data = await listFiles(args.directory_path, args.file_extension);
      return JSON.stringify(data);
      
    } catch (error) {
      console.error('Error in function call handler:', error);
      return JSON.stringify({ 
        error: 'Failed to list files',
        message: error instanceof Error ? error.message : 'Unknown error'
      });
    }
  };

  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <div className={styles.chatContainer}>
          <div className={styles.chat}>
            <Chat functionCallHandler={functionCallHandler} />
          </div>
        </div>
      </div>
    </main>
  );
};

export default FunctionCalling;
