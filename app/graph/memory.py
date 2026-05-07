# import redis
# import json

# # fallback if Redis not running
# try:
#     r = redis.Redis(host="localhost", port=6379, decode_responses=True)
#     r.ping()
# except:
#     r = None


# def save_memory(session_id, data):
#     if r:
#         r.set(session_id, json.dumps(data))


# def load_memory(session_id):
#     if r:
#         val = r.get(session_id)
#         return json.loads(val) if val else []
#     return []