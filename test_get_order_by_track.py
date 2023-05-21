import sender_stand_request
import data

def test_get_order_track():
    resp_track = sender_stand_request.post_new_order(data.order_body)
    track_order = resp_track.json("track_number")
    resp_order = sender_stand_request.get_order(track_order)
    actual_status_code = resp_order.status_code
    expected_status_code = 200
    assert actual_status_code == expected_status_code