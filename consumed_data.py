from dataclasses import dataclass


@dataclass
class ConsumedData(object):
    user_id: int
    mu_custom_id: str = None
    user_address: str = None
    platform: str = None
    signup_at: str = None
    user_name: str = None

    def __int__(self, mu_custom_id, user_id, user_name, user_address, platform, signup_at):
        self.mu_custom_id = mu_custom_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_address = user_address
        self.platform = platform
        self.signup_at = signup_at
