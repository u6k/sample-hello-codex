import runpy
from pathlib import Path


def test_hello_script_outputs_hello(capsys):
    script_path = Path(__file__).resolve().parents[1] / "hello.py"
    runpy.run_path(script_path, run_name="__main__")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
