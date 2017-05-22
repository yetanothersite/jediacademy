from channels.routing import route

from ranking.consumers import send_rank_register_notification


channel_routing = [
    route('send_rank_register_notification', send_rank_register_notification),
]
