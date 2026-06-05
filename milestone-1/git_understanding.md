# Git Understanding 

**Issue Number:** #59
**Milestone:** 1
**Date Completed:** 5/6/26

---

## Goal

Understand what merge conflicts are, why they happen, and how to resolve them.

---

## Reflections

### What caused the conflict?

This merge conflict was caused by the same line in the same file being changed in two different branches. Git was unable to determine which version should be kept when attempting to merge the branches.

For this exercise, I made a branch and edited a file. Then, I went back to the main branch and edited the same line in the same file. I tried to merge the branch into main and Git found conflicting changes and asked me for help.

### How did you resolve it?

I used the merge tools available in VS Code to review both versions of the conflicting code. After comparing the changes, I selected the appropriate resolution and removed the conflict markers.

After the conflict, I did a staged file and made a new commit to complete the merge.


### What did you learn?

This exercise helped me understand how conflicts can be created and how Git resolves conflicts.
Key lessons learned:
* Conflicts occur when two or more branches edit the same section of a file.
* In certain cases, Git is unable to automatically decide which changes should be retained.
* The use of conflict markers allows for pinpointing exactly where the conflicting changes occurred.
* Conflict resolution is easier in editors like VS Code, where you can merge tools.
* Frequent commits, smaller PRs and regularly pulling changes from the main branch can minimize the risk of merge conflicts.

Merge conflicts are typically part of collaborative software development and version control processes, so it is crucial to understand them.


---

## Screenshots

![Branch creation](Screenshots/branch-creation.png)

![Merge conflict error](Screenshots/merge-conflict.png)

![VS Code Merge Editor](Screenshots/merge-editor.png)

![Commit after conflict resolution](Screenshots/resolved.png)