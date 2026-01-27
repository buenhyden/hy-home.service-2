---
description: Systematically resolve "Cannot find module" errors (Import paths & Post-Git Pull)
---

# Debug Module Not Found Errors

This workflow covers resolving "Cannot find module" errors, both during development (import issues) and after pulling changes from Git.

## Part 1: Import Path & Development Issues

1. **Check the Import Path**:
   - ❌ `import { foo } from '../components/Foo'` (missing file extension in some setups)
   - ✅ `import { foo } from '../components/Foo.tsx'` or use path aliases

2. **Verify Module is Installed**:
   - Check if it exists in `node_modules`.
     // turbo
   - Run `ls node_modules/<package-name>`
   - If missing, install it:
     // turbo
   - Run `npm install <package-name>`

3. **Check Case Sensitivity**:
   - macOS/Windows are case-insensitive, but Linux (and CI/CD) is not.
   - ❌ `import Foo from './foo'` when file is `Foo.tsx`
   - ✅ `import Foo from './Foo'`

4. **Check TypeScript Path Aliases**:
   - Ensure `tsconfig.json` paths match your imports.

   ```json
   {
     "compilerOptions": {
       "baseUrl": ".",
       "paths": {
         "@/*": ["./src/*"]
       }
     }
   }
   ```

## Part 2: Post-Git Pull & Dependency Issues

1. **Clear Node Modules Cache**:
   - Remove cached modules and reinstall.
     // turbo
   - Run `rm -rf node_modules .next && npm install`

2. **Check for Lockfile Conflicts**:
   - Look for merge conflicts in package-lock.json.
     // turbo
   - Run `git diff package-lock.json`
   - If conflicted, regenerate: `rm package-lock.json && npm install`

3. **Install Missing Peer Dependencies**:
   - Check for peer dependency warnings.
     // turbo
   - Run `npm install --legacy-peer-deps`

4. **Fix Monorepo/Workspace Issues**:
   - If using pnpm/yarn workspaces, ensure the package is linked or reinstalled from root.
     // turbo
   - Run `pnpm install --force` (or `yarn install`)

5. **Update TypeScript Paths**:
   - Regenerate path mappings if tsconfig changed.
     // turbo
   - Run `npx tsc --noEmit`

## Pro Tips

- Use absolute imports with `@/` to avoid `../../../../` hell.
- Run `npm ls <package-name>` to check which version is installed.
- Click "Restart TS Server" in VS Code command palette if errors persist after fixing.
