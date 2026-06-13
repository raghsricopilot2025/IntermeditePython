from src.intermediate_python.main import main


def test_main_prints(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from IntermediatePython!" in captured.out
