// app/utils/list-files.ts
'use server'

import fs from 'fs';
import path from 'path';

export async function listFiles(directory_path: string, file_extension?: string) {
  try {
    console.log(directory_path)
    console.log(file_extension)
    // Validate and sanitize the directory path
    const normalizedPath = path.normalize(directory_path);
    
    // Ensure the path exists and is a directory
    if (!fs.existsSync(normalizedPath)) {
      throw new Error('Directory does not exist');
    }

    const stats = fs.statSync(normalizedPath);
    if (!stats.isDirectory()) {
      throw new Error('Path is not a directory');
    }

    // Read all files in the directory
    const files = fs.readdirSync(normalizedPath);
    
    // Filter files by extension if provided and create result object
    const result: Record<string, { path: string; contents: string }> = {};
    
    files.forEach((file, index) => {
      const filePath = path.join(normalizedPath, file);
      const stat = fs.statSync(filePath);
      
      if(stat.isFile()) {
        try {
          const contents = fs.readFileSync(filePath, 'utf8');
          result[`file_${index + 1}`] = {
            path: filePath,
            contents: contents
          };
        } catch (err) {
          console.error(`Error reading file ${filePath}:`, err);
        }
      } else {
          result[`file_${index + 1}`] = {
            path: filePath,
            contents: "DIRECTORY"
          };
      }
    });

    return result;
    
  } catch (error) {
    console.error('Error listing files:', error);
    throw error;
  }
}
