from expects import expect, be


class TestDummy:
    def test_dummy(self) -> None:
        expect(True).to(be(True))
