import pytest
from main import merge_and_write


TEST_DATA = "It is my perception that a true friend never relies on anothers dream.A person with the potential to be my true friend must be able to find his own reason for life without my help. And he should put his heart and soul into protecting his dream.He would never hesitate to fight for his dream, even against me.For me, a true friend is one who stands equal to me in all respects."

TEST_DATA_1 = ["It is my perception that a true friend never relies on anothers dream.",
               "A person with the potential to be my true friend must be able to find his own reason for life without my help."]
TEST_DATA_2 = ["And he should put his heart and soul into protecting his dream.",
               "He would never hesitate to fight for his dream, even against me.",
               "For me, a true friend is one who stands equal to me in all respects."]


def create_test_data(test_path, test_data):
    with open(test_path, "w") as f:
        f.writelines(test_data)


@pytest.mark.parametrize(
    "file1, file2, output, result",
    [
        ("test1.txt", "test2.txt", "output.txt", TEST_DATA)
    ]
)
def test_merge_and_write_1(file1, file2, output, result):
    create_test_data(file1, TEST_DATA_1)
    create_test_data(file2, TEST_DATA_2)

    assert merge_and_write(file1, file2, output) == result


@pytest.mark.parametrize(
    "file1, file2, output, result_exception",
    [
        ("test1.txt", "test3.txt", "output.txt", "Один из файлов не найден"),
        ("test3.txt", "test2.txt", "output.txt", "Один из файлов не найден")
    ]
)
def test_merge_and_write_2(file1, file2, output, result_exception):
    assert merge_and_write(file1, file2, output) == "Один из файлов не найден"
