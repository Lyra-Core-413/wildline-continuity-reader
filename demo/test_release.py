"""Public-export boundary tests; only fictional selected-field inputs."""
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('public_h5', ROOT / 'h5_sidecar.py')
h5 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h5)

class ReleaseTests(unittest.TestCase):
    def cli(self, *args):
        return subprocess.run([sys.executable, '-X', 'utf8', '-I', '-B', str(ROOT / 'h5_sidecar.py'),
                               '--json', *args], cwd=ROOT, capture_output=True,
                              text=True, encoding='utf-8', timeout=20)

    def test_external_input_refused_before_any_filesystem_read(self):
        r = self.cli('acquire', '--mode', 'external', '--a', 'absent-A', '--b', 'absent-B',
                     '--run', str(ROOT / 'never-created'), '--scope', 'DEMO/H5/test',
                     '--fact-id', '900000001')
        self.assertEqual(r.returncode, 2)
        self.assertEqual(r.stderr.strip(), 'STOP: EXTERNAL_INPUT_DISABLED_IN_PUBLIC_CANDIDATE')
        self.assertFalse((ROOT / 'never-created').exists())

    def test_external_capture_library_boundary_also_refused(self):
        c = json.loads((ROOT / 'fixtures/A.json').read_bytes())
        c.update(mode='external', provenance={'method': 'external-supplied',
                     'collector': 'fictional', 'origin_status': 'CLAIMED_UNVERIFIED'})
        with self.assertRaisesRegex(h5.Stop, 'EXTERNAL_INPUT_DISABLED_IN_PUBLIC_CANDIDATE'):
            h5.validate_capture(h5.canonical(c), mode='external', stage='A',
                                fact_id=c['fact_id'], scope=c['scope'])

    def test_historical_handoff_has_no_private_absolute_path(self):
        r = self.cli('historical')
        self.assertEqual(r.returncode, 0, r.stderr)
        value = json.loads(r.stdout)
        self.assertFalse(value['executed'])
        self.assertEqual(value['launcher'], 'README.md#evidence-boundaries')
        self.assertIn('not included', value['message'])

    def test_one_command_launches_actual_fresh_process_demo(self):
        r = subprocess.run(['cmd.exe', '/d', '/c', str(ROOT.parent / 'RUN-JUDGE.cmd')],
                            cwd=ROOT, capture_output=True, text=True, encoding='utf-8', timeout=30)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn('SYNTHETIC DEMONSTRATION', r.stdout)
        self.assertIn('Acquisition process exited.', r.stdout)
        self.assertIn('Historical and genuine Bee evidence are not included.', r.stdout)
        self.assertIn('Fictional demo: the display still needs review', r.stdout)
        self.assertIn('Authority: NONE. No actions taken.', r.stdout)

    def test_fixtures_do_not_claim_authentic_origin(self):
        for name in ('A.json', 'B.json'):
            c = json.loads((ROOT / 'fixtures' / name).read_bytes())
            self.assertEqual(c['mode'], 'synthetic')
            self.assertEqual(c['provenance']['origin_status'], 'SYNTHETIC')
            self.assertTrue(c['text'].startswith('Fictional demo:'))

    def test_export_source_omits_private_handoff_and_small_fact_identifiers(self):
        source = (ROOT / 'h5_sidecar.py').read_text(encoding='utf-8')
        self.assertIsNone(re.search(r'[A-Za-z]:\\\\|/home/|/Users/', source))
        self.assertIsNone(re.search(r'\b[0-9]{8}\b', source))

    def test_no_authenticated_adapter_or_binary_is_shipped(self):
        self.assertFalse((ROOT.parent / 'bee_runtime.py').exists())
        for p in ROOT.parent.rglob('*'):
            if p.is_file():
                self.assertNotIn(p.suffix.lower(), ('.exe', '.dll', '.pyd', '.zip', '.db', '.sqlite'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
