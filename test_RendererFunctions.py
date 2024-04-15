import RainbowRendererMain


def test_StandardScreenSizes():
    assert RainbowRendererMain.getStandardScreenDefinitions("landscape", "HD") == (
        1920,
        1080,
    )
    assert RainbowRendererMain.getStandardScreenDefinitions("portrait", "HD") == (
        1080,
        1920,
    )


def test_normalizedPixelPositions():
    assert RainbowRendererMain.getNormalizedPixelPositions((100, 100))["x"][0] == 0
    assert RainbowRendererMain.getNormalizedPixelPositions((100, 100))["x"][99] == 1.0
    assert RainbowRendererMain.getNormalizedPixelPositions((100, 100))["y"][0] == 0
    assert RainbowRendererMain.getNormalizedPixelPositions((100, 100))["y"][99] == 1.0


def test_normalizeTo8Bit():
    assert RainbowRendererMain.normalizeTo8Bit(1.012) == 255
    assert RainbowRendererMain.normalizeTo8Bit(264.4312) == 255
    assert RainbowRendererMain.normalizeTo8Bit(0.998) == 254
    assert RainbowRendererMain.normalizeTo8Bit(-0.25) == 255


def test_getNormalizedPixelPositions_negative_imageSizes():
    try:
        getNormalizedPixelPositions((-1, -1))
        assert False, "Expected an exception for negative image sizes"
    except Exception as e:
        assert str(e) == "division by zero", f"Unexpected exception message: {e}"