/*
 * workspaceEditUtils.ts
 * Copyright (c) Microsoft Corporation.
 * Licensed under the MIT license.
 *
 * Convert Pyright's FileEditActions to LanguageServer's WorkspaceEdits.
 */

import type { WorkspaceEdit } from 'vscode-languageserver';

import type { FileEditAction } from '../common/editAction';
import { convertPathToUri } from '../common/pathUtils';
import type { FileSystem } from './fileSystem';

export function convertWorkspaceEdits(fs: FileSystem, edits: FileEditAction[]) {
    const workspaceEdits: WorkspaceEdit = {
        changes: {},
    };

    edits.forEach((edit) => {
        const uri = convertPathToUri(fs, edit.filePath);
        workspaceEdits.changes![uri] = workspaceEdits.changes![uri] || [];
        workspaceEdits.changes![uri].push({ range: edit.range, newText: edit.replacementText });
    });

    return workspaceEdits;
}
