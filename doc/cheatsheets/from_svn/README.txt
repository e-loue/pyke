Here's how I got there (all directories relative to
~/python/workareas/pyke-hg-convert):

1.  Copied svn repo from sourceforge to the "pykemirror" directory:

2.  Ran "hg convert" using pyke.filemap and pyke.splicemap (both in
    ~/python/workareas/pyke-hg-convert) to produce sf.3 hg repo.

3.  Do "hg rollback" in sf.3 to undo the commit of .hgtags done by "hg convert".

4.  hg clone sf.3 trial.3

    (make sure you got updated to the tip, the last changeset for the
     "release_1.0" branch, and not the last "default" branch).

5.  Add username to trial.3/.hg/hgrc

6.  mv sf.3/.hgtags trial.3

7.  Copy pyke.filemap, pyke.splicemap and sf.3/.hg/shamap to
    trial.3/doc/cheatsheets/from_svn

8.  Set up hg keywords, create trial.3/hgrc_keywords, add to trial.3/.hg/hgrc

9.  Create trial.3/.hgignore

10. Change test scripts:

    Test/testTest
    doc/testdocs
    examples/testexamples
    pyke/testpyke

    to automatically set PYTHONPATH to be able to run from any clone.

11. Extraneous change to examples/family_relations/family.kfb for keyword
    expansion problem.

12. Remove .svn directories from:

    Test/testTest
    examples/testexamples
    make_doc_tarball
    make_examples_tarball

13. Commit all changes to trial.3

14. hg convert --config convert.hg.clonebranches=True \
               --config convert.hg.usebranchnames=0 trial.3 split

15. Go into split/release_1.0:

    A.  "hg rollback" the .hgtags commit
    B.  Move .hgtags somewhere else
    C.  hg update tip
    D.  Move .hgtags back
    E.  join
          split/release_1.0/doc/cheatsheets/from_svn/shamap
        and
          split/.hg/shamap
        to update the hg ids (since these have been reassigned in the split)
    F.  Add username to .hg/hgrc
    G.  hg commit

16. Remove the named branches from split/release_1.0 and split/pre_2to3:

    mkdir no_branches_1
    hg convert --branchmap branchmap split/release_1.0 no_branches_1/release_1
    hg convert --branchmap branchmap split/pre_2to3 no_branches_1/pre_2to3

    We don't need:

      split/default -- because it's the same as release_1.0
      split/zope -- the person can do his own repo to work on this now

    This reassigns the hg ids (again), but assigns the same ids to shared
    changesets between no_branches_1/release_1 and no_branches_1/pre_2to3.

17. Go into no_branches_1/release_1 and update doc/cheatsheets/from_svn/shamap
    using both no_branches_1/{release_1,pre_2to3}/.hg/shamap to convert.  The
    .hgtags file gets converted automatically by "hg convert" without it doing
    a commit this time...

    Make sure you update the username in no_branches_1/release_1/.hg/hgrc
    prior to committing.

18. Create a release_1 and pre_2to3 repository on sourceforge (shell interface)
    and push the two no_branches_1 repos to sourceforge.

19. Using the shell interface, clone release_1 on sourceforge to create the
    pyke repo on sourceforge.

