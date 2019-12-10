import logging

import log_file


def assert_common(s, response, status_code=200, message="操作成功！"):
    try:
        # 断言状态码
        s.assertEqual(status_code, response.status_code)
        # 断言 success
        s.assertTrue(response.json().get("success"))
        # 断言 code
        s.assertEqual(10000, response.json().get("code"))
        # 断言 message
        s.assertEqual(message, response.json().get("message"))
    except Exception as e:
        logging.error(f"{e}")
        raise e
