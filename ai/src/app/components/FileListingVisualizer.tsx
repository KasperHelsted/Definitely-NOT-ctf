import { useState } from 'react';
import { ChevronRight, ChevronDown, Folder, File } from 'lucide-react';

type FileData = {
  path: string;
  contents: string;
};

type FileListingData = {
  [key: string]: FileData;
};

const FileListingVisualizer = ({ data }: { data: FileListingData }) => {
  const [expandedPaths, setExpandedPaths] = useState<Set<string>>(new Set());

  const groupByDirectory = (files: FileListingData) => {
    const directoryStructure: Record<string, FileData[]> = {};
    
    Object.values(files).forEach(file => {
      const dirPath = file.path.split('/').slice(0, -1).join('/');
      if (!directoryStructure[dirPath]) {
        directoryStructure[dirPath] = [];
      }
      directoryStructure[dirPath].push(file);
    });
    
    return directoryStructure;
  };

  const togglePath = (path: string) => {
    const newExpanded = new Set(expandedPaths);
    if (expandedPaths.has(path)) {
      newExpanded.delete(path);
    } else {
      newExpanded.add(path);
    }
    setExpandedPaths(newExpanded);
  };

  const RenderItem = ({ path, isDirectory, items }: { 
    path: string;
    isDirectory: boolean;
    items?: FileData[];
  }) => {
    const isExpanded = expandedPaths.has(path);
    const displayName = path.split('/').pop() || path;

    return (
      <div className="ml-4">
        <div 
          className="flex items-center gap-2 hover:bg-gray-100 p-1 rounded cursor-pointer"
          onClick={() => isDirectory && togglePath(path)}
        >
          {isDirectory ? (
            <>
              {isExpanded ? <ChevronDown size={16} /> : <ChevronRight size={16} />}
              <Folder size={16} className="text-blue-500" />
              <span className="font-medium">{displayName}/</span>
            </>
          ) : (
            <>
              <div className="w-4" /> {/* Spacing for alignment */}
              <File size={16} className="text-gray-500" />
              <span>{displayName}</span>
            </>
          )}
        </div>
        
        {isDirectory && isExpanded && items && (
          <div className="ml-4">
            {items.map((file, index) => (
              <RenderItem
                key={index}
                path={file.path}
                isDirectory={false}
              />
            ))}
          </div>
        )}
      </div>
    );
  };

  const directoryStructure = groupByDirectory(data);

  return (
    <div className="bg-white rounded-lg shadow p-4 mb-4 max-h-[300px] overflow-auto">
      <div className="text-sm font-medium mb-2">File Listing Results</div>
      {Object.entries(directoryStructure).map(([dirPath, files], index) => (
        <RenderItem
          key={index}
          path={dirPath}
          isDirectory={true}
          items={files}
        />
      ))}
    </div>
  );
};

export default FileListingVisualizer;