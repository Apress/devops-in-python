def test_scale():
    result = scale_one(3, 7)
    assert_that(result,
                any_of(divisible_by(3),
                       divisible_by(7)))