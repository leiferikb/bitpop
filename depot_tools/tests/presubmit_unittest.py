import functools
import itertools
import unittest
import subprocess2 as subprocess
  presubmit_trymaster = """
def GetPreferredTryMasters(project, change):
  return %s
"""

    self.mox.StubOutWithMock(presubmit.scm.GIT, 'GenerateDiff')
      'GetTrySlavesExecuter', 'GitAffectedFile', 'CallCommand', 'CommandData',
      'NonexistantCannedCheckFilter', 'OutputApi', 'ParseFiles',
      'PresubmitFailure', 'PresubmitExecuter', 'PresubmitOutput', 'ScanSubDirs',
      'SvnAffectedFile', 'SvnChange', 'cPickle', 'cpplint', 'cStringIO',
      'contextlib', 'canned_check_filter', 'fix_encoding', 'fnmatch',
      'gclient_utils', 'glob', 'inspect', 'json', 'load_files', 'logging',
      'marshal', 'normpath', 'optparse', 'os', 'owners', 'pickle',
      'subprocess', 'sys', 'tempfile', 'time', 'traceback', 'types', 'unittest',
      'urllib2', 'warn', 'multiprocessing', 'DoGetTryMasters',
      'GetTryMastersExecuter', 'itertools',
  def testCannedCheckFilter(self):
    canned = presubmit.presubmit_canned_checks
    orig = canned.CheckOwners
    with presubmit.canned_check_filter(['CheckOwners']):
      self.assertNotEqual(canned.CheckOwners, orig)
      self.assertEqual(canned.CheckOwners(None, None), [])
    self.assertEqual(canned.CheckOwners, orig)

  def testCannedCheckFilterFail(self):
    canned = presubmit.presubmit_canned_checks
    orig = canned.CheckOwners
    def failAttempt():
      with presubmit.canned_check_filter(['CheckOwners', 'Spazfleem']):
        pass
    self.assertRaises(presubmit.NonexistantCannedCheckFilter, failAttempt)
    self.assertEqual(canned.CheckOwners, orig)

  def testGitChange(self):
    description_lines = ('Hello there',
                         'this is a change',
                         'BUG=123',
                         ' STORY =http://foo/  \t',
                         'and some more regular text  \t')
    unified_diff = [
        'diff --git binary_a.png binary_a.png',
        'new file mode 100644',
        'index 0000000..6fbdd6d',
        'Binary files /dev/null and binary_a.png differ',
        'diff --git binary_d.png binary_d.png',
        'deleted file mode 100644',
        'index 6fbdd6d..0000000',
        'Binary files binary_d.png and /dev/null differ',
        'diff --git binary_md.png binary_md.png',
        'index 6fbdd6..be3d5d8 100644',
        'GIT binary patch',
        'delta 109',
        'zcmeyihjs5>)(Opwi4&WXB~yyi6N|G`(i5|?i<2_a@)OH5N{Um`D-<SM@g!_^W9;SR',
        'zO9b*W5{pxTM0slZ=F42indK9U^MTyVQlJ2s%1BMmEKMv1Q^gtS&9nHn&*Ede;|~CU',
        'CMJxLN',
        '',
        'delta 34',
        'scmV+-0Nww+y#@BX1(1W0gkzIp3}CZh0gVZ>`wGVcgW(Rh;SK@ZPa9GXlK=n!',
        '',
        'diff --git binary_m.png binary_m.png',
        'index 6fbdd6d..be3d5d8 100644',
        'Binary files binary_m.png and binary_m.png differ',
        'diff --git boo/blat.cc boo/blat.cc',
        'new file mode 100644',
        'index 0000000..37d18ad',
        '--- boo/blat.cc',
        '+++ boo/blat.cc',
        '@@ -0,0 +1,5 @@',
        '+This is some text',
        '+which lacks a copyright warning',
        '+but it is nonetheless interesting',
        '+and worthy of your attention.',
        '+Its freshness factor is through the roof.',
        'diff --git floo/delburt.cc floo/delburt.cc',
        'deleted file mode 100644',
        'index e06377a..0000000',
        '--- floo/delburt.cc',
        '+++ /dev/null',
        '@@ -1,14 +0,0 @@',
        '-This text used to be here',
        '-but someone, probably you,',
        '-having consumed the text',
        '-  (absorbed its meaning)',
        '-decided that it should be made to not exist',
        '-that others would not read it.',
        '-  (What happened here?',
        '-was the author incompetent?',
        '-or is the world today so different from the world',
        '-   the author foresaw',
        '-and past imaginination',
        '-   amounts to rubble, insignificant,',
        '-something to be tripped over',
        '-and frustrated by)',
        'diff --git foo/TestExpectations foo/TestExpectations',
        'index c6e12ab..d1c5f23 100644',
        '--- foo/TestExpectations',
        '+++ foo/TestExpectations',
        '@@ -1,12 +1,24 @@',
        '-Stranger, behold:',
        '+Strange to behold:',
        '   This is a text',
        ' Its contents existed before.',
        '',
        '-It is written:',
        '+Weasel words suggest:',
        '   its contents shall exist after',
        '   and its contents',
        ' with the progress of time',
        ' will evolve,',
        '-   snaillike,',
        '+   erratically,',
        ' into still different texts',
        '-from this.',
        '\ No newline at end of file',
        '+from this.',
        '+',
        '+For the most part,',
        '+I really think unified diffs',
        '+are elegant: the way you can type',
        '+diff --git inside/a/text inside/a/text',
        '+or something silly like',
        '+@@ -278,6 +278,10 @@',
        '+and have this not be interpreted',
        '+as the start of a new file',
        '+or anything messed up like that,',
        '+because you parsed the header',
        '+correctly.',
        '\ No newline at end of file',
            '']
    files = [('A      ', 'binary_a.png'),
             ('D      ', 'binary_d.png'),
             ('M      ', 'binary_m.png'),
             ('M      ', 'binary_md.png'),  # Binary w/ diff
             ('A      ', 'boo/blat.cc'),
             ('D      ', 'floo/delburt.cc'),
             ('M      ', 'foo/TestExpectations')]

    for op, path in files:
      full_path = presubmit.os.path.join(self.fake_root_dir, *path.split('/'))
      if op.startswith('D'):
        os.path.exists(full_path).AndReturn(False)
      else:
        os.path.exists(full_path).AndReturn(False)
        os.path.isfile(full_path).AndReturn(True)

    presubmit.scm.GIT.GenerateDiff(
        self.fake_root_dir, files=[], full_move=True, branch=None
        ).AndReturn('\n'.join(unified_diff))

    self.mox.ReplayAll()

    change = presubmit.GitChange(
        'mychange',
        '\n'.join(description_lines),
        self.fake_root_dir,
        files,
        0,
        0,
        None,
        upstream=None)
    self.failUnless(change.Name() == 'mychange')
    self.failUnless(change.DescriptionText() ==
                    'Hello there\nthis is a change\nand some more regular text')
    self.failUnless(change.FullDescriptionText() ==
                    '\n'.join(description_lines))

    self.failUnless(change.BUG == '123')
    self.failUnless(change.STORY == 'http://foo/')
    self.failUnless(change.BLEH == None)

    self.failUnless(len(change.AffectedFiles()) == 7)
    self.failUnless(len(change.AffectedFiles(include_dirs=True)) == 7)
    self.failUnless(len(change.AffectedFiles(include_deletes=False)) == 5)
    self.failUnless(len(change.AffectedFiles(include_dirs=True,
                                             include_deletes=False)) == 5)

    # Note that on git, there's no distinction between binary files and text
    # files; everything that's not a delete is a text file.
    affected_text_files = change.AffectedTextFiles()
    self.failUnless(len(affected_text_files) == 5)

    local_paths = change.LocalPaths()
    expected_paths = [os.path.normpath(f) for op, f in files]
    self.assertEqual(local_paths, expected_paths)

    try:
      _ = change.ServerPaths()
      self.fail("ServerPaths implemented.")
    except NotImplementedError:
      pass

    actual_rhs_lines = []
    for f, linenum, line in change.RightHandSideLines():
      actual_rhs_lines.append((f.LocalPath(), linenum, line))

    f_blat = os.path.normpath('boo/blat.cc')
    f_test_expectations = os.path.normpath('foo/TestExpectations')
    expected_rhs_lines = [
        (f_blat, 1, 'This is some text'),
        (f_blat, 2, 'which lacks a copyright warning'),
        (f_blat, 3, 'but it is nonetheless interesting'),
        (f_blat, 4, 'and worthy of your attention.'),
        (f_blat, 5, 'Its freshness factor is through the roof.'),
        (f_test_expectations, 1, 'Strange to behold:'),
        (f_test_expectations, 5, 'Weasel words suggest:'),
        (f_test_expectations, 10, '   erratically,'),
        (f_test_expectations, 13, 'from this.'),
        (f_test_expectations, 14, ''),
        (f_test_expectations, 15, 'For the most part,'),
        (f_test_expectations, 16, 'I really think unified diffs'),
        (f_test_expectations, 17, 'are elegant: the way you can type'),
        (f_test_expectations, 18, 'diff --git inside/a/text inside/a/text'),
        (f_test_expectations, 19, 'or something silly like'),
        (f_test_expectations, 20, '@@ -278,6 +278,10 @@'),
        (f_test_expectations, 21, 'and have this not be interpreted'),
        (f_test_expectations, 22, 'as the start of a new file'),
        (f_test_expectations, 23, 'or anything messed up like that,'),
        (f_test_expectations, 24, 'because you parsed the header'),
        (f_test_expectations, 25, 'correctly.')]

    self.assertEquals(expected_rhs_lines, actual_rhs_lines)

    text = (
        'Running presubmit upload checks ...\n'
        'Warning, no PRESUBMIT.py found.\n'
        'Running default presubmit script.\n'
        '\n'
        '** Presubmit ERRORS **\n!!\n\n'
        'Was the presubmit check useful? If not, run "git cl presubmit -v"\n'
        'to figure out which PRESUBMIT.py was run, then run git blame\n'
        'on the file to figure out who to ask for help.\n')
    mixed_old_and_new = ['bot', ('bot2', set(['test']))]
    not_set = [('bot2', ['test'])]
    for result in (
        starts_with_space_result, not_list_result1, not_list_result2,
        mixed_old_and_new, not_set):
    new_style = [('bot', set(['cool', 'tests']))]
    for result in (
        expected_result, empty_result, space_in_name_result, new_style):
  def testGetTryMastersExecuter(self):
    self.mox.ReplayAll()
    change = presubmit.Change(
        'foo',
        'Blah Blah\n\nSTORY=http://tracker.com/42\nBUG=boo\n',
        self.fake_root_dir,
        None,
        0,
        0,
        None)
    executer = presubmit.GetTryMastersExecuter()
    self.assertEqual({}, executer.ExecPresubmitScript('', '', '', change))
    self.assertEqual({},
        executer.ExecPresubmitScript('def foo():\n  return\n', '', '', change))

    expected_result = {'m1': {'s1': set(['t1', 't2'])},
                       'm2': {'s1': set(['defaulttests']),
                              's2': set(['defaulttests'])}}
    empty_result1 = {}
    empty_result2 = {'m': {}}
    space_in_name_result = {'m r': {'s\tv': set(['t1'])}}
    for result in (
        expected_result, empty_result1, empty_result2, space_in_name_result):
      self.assertEqual(
          result,
          executer.ExecPresubmitScript(
              self.presubmit_trymaster % result, '', '', change))

  def testMergeMasters(self):
    merge = presubmit._MergeMasters
    self.assertEqual({}, merge({}, {}))
    self.assertEqual({'m1': {}}, merge({}, {'m1': {}}))
    self.assertEqual({'m1': {}}, merge({'m1': {}}, {}))
    parts = [
      {'try1.cr': {'win': set(['defaulttests'])}},
      {'try1.cr': {'linux1': set(['test1'])},
       'try2.cr': {'linux2': set(['defaulttests'])}},
      {'try1.cr': {'mac1': set(['defaulttests']),
                   'mac2': set(['test1', 'test2']),
                   'linux1': set(['defaulttests'])}},
    ]
    expected = {
      'try1.cr': {'win': set(['defaulttests']),
                  'linux1': set(['defaulttests', 'test1']),
                  'mac1': set(['defaulttests']),
                  'mac2': set(['test1', 'test2'])},
      'try2.cr': {'linux2': set(['defaulttests'])},
    }
    for permutation in itertools.permutations(parts):
      self.assertEqual(expected, reduce(merge, permutation, {}))

  def testDoGetTryMasters(self):
    root_text = (self.presubmit_trymaster
        % '{"t1.cr": {"win": set(["defaulttests"])}}')
    linux_text = (self.presubmit_trymaster
        % ('{"t1.cr": {"linux1": set(["t1"])},'
           ' "t2.cr": {"linux2": set(["defaulttests"])}}'))

    join = presubmit.os.path.join
    isfile = presubmit.os.path.isfile
    FileRead = presubmit.gclient_utils.FileRead
    filename = 'foo.cc'
    filename_linux = join('linux_only', 'penguin.cc')
    root_presubmit = join(self.fake_root_dir, 'PRESUBMIT.py')
    linux_presubmit = join(self.fake_root_dir, 'linux_only', 'PRESUBMIT.py')
    inherit_path = join(self.fake_root_dir, self._INHERIT_SETTINGS)

    isfile(inherit_path).AndReturn(False)
    isfile(root_presubmit).AndReturn(True)
    FileRead(root_presubmit, 'rU').AndReturn(root_text)

    isfile(inherit_path).AndReturn(False)
    isfile(root_presubmit).AndReturn(True)
    isfile(linux_presubmit).AndReturn(True)
    FileRead(root_presubmit, 'rU').AndReturn(root_text)
    FileRead(linux_presubmit, 'rU').AndReturn(linux_text)
    self.mox.ReplayAll()

    change = presubmit.Change(
        'mychange', '', self.fake_root_dir, [], 0, 0, None)

    output = StringIO.StringIO()
    self.assertEqual({'t1.cr': {'win': ['defaulttests']}},
                     presubmit.DoGetTryMasters(change, [filename],
                                               self.fake_root_dir,
                                               None, None, False, output))
    output = StringIO.StringIO()
    expected = {
      't1.cr': {'win': ['defaulttests'], 'linux1': ['t1']},
      't2.cr': {'linux2': ['defaulttests']},
    }
    self.assertEqual(expected,
                     presubmit.DoGetTryMasters(change,
                                               [filename, filename_linux],
                                               self.fake_root_dir, None, None,
                                               False, output))

      'LocalToDepotPath', 'Command', 'RunTests',
      'basename', 'cPickle', 'cpplint', 'cStringIO', 'canned_checks', 'change',
      'environ', 'glob', 'host_url', 'is_committing', 'json', 'logging',
      'marshal', 'os_listdir', 'os_walk', 'os_path', 'owners_db', 'pickle',
      'platform', 'python_executable', 're', 'rietveld', 'subprocess', 'tbr',
      'tempfile', 'time', 'traceback', 'unittest', 'urllib2', 'version',
      'verbose',
      ['D', join('foo', 'mat', 'beingdeleted.txt')],
      ['M', join('flop', 'notfound.txt')],
      ['A', join('boo', 'flap.h')],
      return presubmit.AffectedFile(x, 'M', self.fake_root_dir, None)
    fileobj = presubmit.AffectedFile('boo', 'M', 'Unrelated',
                                     diff_cache=mox.IsA(presubmit._DiffCache))
    fileobj = presubmit.AffectedFile('AA/boo', 'M', self.fake_root_dir,
                                     diff_cache=mox.IsA(presubmit._DiffCache))
class OutputApiUnittest(PresubmitTestsBase):

      'PresubmitNotifyResult', 'PresubmitPromptWarning',
      'PresubmitPromptOrNotify', 'PresubmitResult', 'is_committing',
    self.compareMembers(presubmit.OutputApi(False), members)
    output = presubmit.PresubmitOutput(input_stream=StringIO.StringIO('\n'))
    self.failIf(output.should_continue())
    self.failUnless(output.getvalue().count('???'))

    output_api = presubmit.OutputApi(True)
    output = presubmit.PresubmitOutput(input_stream=StringIO.StringIO('y'))
    output_api.PresubmitPromptOrNotify('???').handle(output)
    output.prompt_yes_no('prompt: ')
    output_api = presubmit.OutputApi(False)
    output = presubmit.PresubmitOutput(input_stream=StringIO.StringIO('y'))
    output_api.PresubmitPromptOrNotify('???').handle(output)
    self.failUnless(output.should_continue())
    self.failUnless(output.getvalue().count('???'))

    output_api = presubmit.OutputApi(True)
    output_api.PresubmitPromptOrNotify('???').handle(output)
      'AbsoluteLocalPath', 'Action', 'ChangedContents', 'DIFF_CACHE',
      'GenerateScmDiff', 'IsDirectory', 'IsTextFile', 'LocalPath',
      'NewContents', 'Property', 'ServerPath',
        presubmit.AffectedFile('a', 'b', self.fake_root_dir, None), members)
    self.compareMembers(
        presubmit.SvnAffectedFile('a', 'b', self.fake_root_dir, None), members)
        presubmit.GitAffectedFile('a', 'b', self.fake_root_dir, None), members)
    af = presubmit.SvnAffectedFile('foo/blat.cc', 'M', self.fake_root_dir, None)
    af = presubmit.AffectedFile(notfound, 'A', self.fake_root_dir, None)
    affected_file = presubmit.SvnAffectedFile('foo.cc', 'A', self.fake_root_dir,
                                              None)
    affected_file = presubmit.SvnAffectedFile(filename, 'A', self.fake_root_dir,
                                              None)
    affected_file = presubmit.SvnAffectedFile(filename, 'A', self.fake_root_dir,
                                              None)
        presubmit.SvnAffectedFile('foo/blat.txt', 'M', self.fake_root_dir,
                                  None),
        presubmit.SvnAffectedFile('foo/binary.blob', 'M', self.fake_root_dir,
                                  None),
        presubmit.SvnAffectedFile('blat/flop.txt', 'D', self.fake_root_dir,
                                  None)
        'SetDescriptionText', 'TAG_LINE_RE',
  def testSetDescriptionText(self):
    change = presubmit.Change(
        '', 'foo\nDRU=ro', self.fake_root_dir, [], 3, 5, '')
    self.assertEquals('foo', change.DescriptionText())
    self.assertEquals('foo\nDRU=ro', change.FullDescriptionText())
    self.assertEquals('ro', change.DRU)

    change.SetDescriptionText('bar\nWHIZ=bang')
    self.assertEquals('bar', change.DescriptionText())
    self.assertEquals('bar\nWHIZ=bang', change.FullDescriptionText())
    self.assertEquals('bang', change.WHIZ)
    self.assertFalse(change.DRU)


def CommHelper(input_api, cmd, ret=None, **kwargs):
  ret = ret or (('', None), 0)
  input_api.subprocess.communicate(
      cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, **kwargs
      ).AndReturn(ret)

    input_api.subprocess = self.mox.CreateMock(subprocess)
    presubmit.subprocess = input_api.subprocess
    input_api.Command = presubmit.CommandData
    input_api.RunTests = functools.partial(
        presubmit.InputApi.RunTests, input_api)
      'CheckPatchFormatted',
      'GetPythonUnitTests', 'GetPylint',
      'GetUnitTests', 'GetUnitTestsInDirectory',
      presubmit.SvnAffectedFile('foo/bar.cc', 'A', self.fake_root_dir, None),
      presubmit.SvnAffectedFile('foo.cc', 'M', self.fake_root_dir, None),
      presubmit.SvnAffectedFile('foo/bar.cc', 'A', self.fake_root_dir, None),
      presubmit.SvnAffectedFile('foo.cc', 'M', self.fake_root_dir, None),
        'makefile.foo:46')
    check = lambda x, y, _: presubmit_canned_checks.CheckLongLines(x, y, 80)
    check = lambda x, y, _: presubmit_canned_checks.CheckLongLines(x, y, 80)
  def testCannedCheckObjCExceptionLongLines(self):
    check = lambda x, y, _: presubmit_canned_checks.CheckLongLines(x, y, 80)
    self.ContentTest(check, '#import ' + 'A ' * 150, 'foo.mm',
                     'import' + 'A ' * 150, 'foo.mm',
                     presubmit.OutputApi.PresubmitPromptWarning)

  def testCannedCheckMakefileLongLines(self):
    check = lambda x, y, _: presubmit_canned_checks.CheckLongLines(x, y, 80)
    self.ContentTest(check, 'A ' * 100, 'foo.mk', 'A ' * 100 + 'B', 'foo.mk',
                     presubmit.OutputApi.PresubmitPromptWarning)

  def testCannedCheckCppExceptionLongLines(self):
        '#if 56 89 12 45 9191919191919',
        'foo.cc',
        '#nif 56 89 12 45 9191919191919',
        'foo.cc',
  def testCannedCheckLongLinesFile(self):
    check = lambda x, y, z: presubmit_canned_checks.CheckLongLines(x, y, 10, z)
    self.ContentTest(
        check,
        ' file:// 0 23 5',
        None,
        ' file:// 0 23 56',
        None,
        presubmit.OutputApi.PresubmitPromptWarning)


    output_api = presubmit.OutputApi(False)
    A = lambda x: presubmit.AffectedFile(x, 'M', self.fake_root_dir, None)
    CommHelper(input_api, ['pyyyyython', '-m', '_non_existent_module'],
                    ret=(('foo', None), 1), cwd=None, env=None)
    CommHelper(input_api, ['pyyyyython', '-m', '_non_existent_module'],
                    ret=(('foo', None), 1), cwd=None, env=None)
    CommHelper(input_api, ['pyyyyython', '-m', 'test_module'],
                    ret=(('foo', None), 1), cwd=None, env=None)
    self.assertEquals('test_module (0.00s) failed\nfoo', results[0]._message)
    CommHelper(input_api, ['pyyyyython', '-m', 'test_module'],
                    ret=(('foo', None), 1), cwd=None, env=None)
    self.assertEquals('test_module (0.00s) failed\nfoo', results[0]._message)
    CommHelper(input_api, ['pyyyyython', '-m', 'test_module'],
                    cwd=None, env=None)
    CommHelper(input_api,
        ['pyyyyython', pylint, '--args-on-stdin'],
        env=mox.IgnoreArg(), stdin='file1.py\n--rcfile=%s' % pylintrc)
    self.checkstdout('')
      uncovered_files=None, expected_output='', author_counts_as_owner=True,
      manually_specified_reviewers=None):
      # The set of people who lgtm'ed a change.
      # The set of people needed to lgtm a change. We default to
      # the same list as the people who approved it. We use 'reviewers'
      # to avoid a name collision w/ owners.py.
      reviewers = approvers
    if uncovered_files is None:
      uncovered_files = set()
    if manually_specified_reviewers is None:
      manually_specified_reviewers = []
    change.author_email = 'john@example.com'
    change.R = ','.join(manually_specified_reviewers)
    change.TBR = ''
      if issue and not rietveld_response:
          "owner_email": change.author_email,
      if author_counts_as_owner:
        people.add(change.author_email)
        fake_db.files_not_covered_by(set(['foo/xyz.cc']),
            people).AndReturn(uncovered_files)
      else:
        people.discard(change.author_email)
        fake_db.files_not_covered_by(set(['foo/xyz.cc']),
            people).AndReturn(uncovered_files)
      if not is_committing and uncovered_files:
        fake_db.reviewers_for(set(['foo']),
            change.author_email).AndReturn(change.author_email)
        presubmit.OutputApi, author_counts_as_owner=author_counts_as_owner)
        uncovered_files=set(['foo']),
        expected_output="OWNERS check failed: this change has no Rietveld "
                        "issue number, so we can't check it for approvals.\n")
    self.AssertOwnersWorks(issue=None,
        is_committing=False,
        uncovered_files=set(['foo']),
        expected_output='Missing OWNER reviewers for these files:\n'
                        '    foo\n')

  def testCannedCheckOwners_NoIssueLocalReviewers(self):
    self.AssertOwnersWorks(issue=None,
        reviewers=set(['jane@example.com']),
        manually_specified_reviewers=['jane@example.com'],
        expected_output="OWNERS check failed: this change has no Rietveld "
                        "issue number, so we can't check it for approvals.\n")
    self.AssertOwnersWorks(issue=None,
        reviewers=set(['jane@example.com']),
        manually_specified_reviewers=['jane@example.com'],
        is_committing=False,
        expected_output='')

  def testCannedCheckOwners_NoIssueLocalReviewersDontInferEmailDomain(self):
    self.AssertOwnersWorks(issue=None,
        reviewers=set(['jane']),
        manually_specified_reviewers=['jane@example.com'],
        uncovered_files=set(['foo']),
        manually_specified_reviewers=['jane'],
        expected_output='Missing OWNER reviewers for these files:\n'
                        '    foo\n')
  def testCannedCheckOwners_AuthorCountsAsOwner(self):
    self.AssertOwnersWorks(approvers=set(['john@example.com',
                                          'brett@example.com']),
                           reviewers=set(['john@example.com',
                                          'ben@example.com']),
                           uncovered_files=set(['foo/xyz.cc', 'foo/bar.cc']),
                           expected_output='Missing LGTM from an OWNER '
                                           'for these files:\n'
                                           '    foo/bar.cc\n'
                                           '    foo/xyz.cc\n',
                           author_counts_as_owner=False)

    self.AssertOwnersWorks(uncovered_files=set(['foo']),
        expected_output='Missing LGTM from an OWNER for these files:\n'
    self.AssertOwnersWorks(uncovered_files=set(['foo']),
        is_committing=False,
        expected_output='Missing OWNER reviewers for these files:\n'
                           uncovered_files=set())
                           uncovered_files=set())
    CommHelper(input_api, ['allo', '--verbose'], cwd=self.fake_root_dir)
    CommHelper(input_api, cmd, cwd=self.fake_root_dir, ret=(('', None), 1))
    self.assertEqual(2, len(results))
        presubmit.OutputApi.PresubmitNotifyResult, results[0].__class__)
    self.assertEqual(
        presubmit.OutputApi.PresubmitPromptWarning, results[1].__class__)
    self.checkstdout('')
    CommHelper(
        input_api,
    self.assertEqual(1, len(results))
    self.assertEqual(
        presubmit.OutputApi.PresubmitNotifyResult, results[0].__class__)
    self.checkstdout('')