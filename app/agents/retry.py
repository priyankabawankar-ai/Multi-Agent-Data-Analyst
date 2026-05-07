# def retry_agent(state):
#     validation = state.get("validation", "").lower()

#     if "no" in validation:
#         print("🔁 Retrying with fallback logic")

#         # fallback → force analyst
#         return {
#             "next_step": "analyst"
#         }

#     return {
#         "next_step": "reporter"
#     }