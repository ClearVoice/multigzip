import pytest
from io import BytesIO

from multigzip import GzipFile


@pytest.fixture
def file_obj():
    fo = BytesIO()
    yield fo
    fo.close()
    del fo


def test_multigzip(file_obj):
    with GzipFile(fileobj=file_obj, mode='wb') as wf:
        wf.write_member(b'Hello World 1')
        wf.write_member(b'Hello World 2')
        wf.write_member(b'Hello World 3')

    file_obj.seek(0)

    with GzipFile(fileobj=file_obj, mode='rb') as rf:
        assert rf.read_member().read() == b'Hello World 1'
        assert rf.read_member().read() == b'Hello World 2'
        assert rf.read_member().read() == b'Hello World 3'
