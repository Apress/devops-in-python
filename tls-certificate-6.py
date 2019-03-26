>>> today = datetime.date.today()
>>> yesterday = today - one_day
>>> builder = builder.not_valid_before(yesterday)