import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Environment (default to DEV)
    environment: str = os.getenv("ENV", "DEV").upper()

    # Development Environment
    dev_mongo_user: str = os.getenv("MONGO_USER_DEV")
    dev_mongo_password: str = os.getenv("MONGO_PW_DEV")
    dev_mongo_host: str = os.getenv("MONGO_HOST_DEV")
    dev_mongo_port: int = int(os.getenv("MONGO_PORT_DEV", 27017))

    # Test Environment
    test_mongo_user: str = os.getenv("MONGO_USER_TEST")
    test_mongo_password: str = os.getenv("MONGO_PW_TEST")
    test_mongo_host: str = os.getenv("MONGO_HOST_TEST")
    test_mongo_port: int = int(os.getenv("MONGO_PORT_TEST", 27018))

    # Production Environment
    prod_mongo_user: str = os.getenv("MONGO_USER_PROD")
    prod_mongo_password: str = os.getenv("MONGO_PW_PROD")
    prod_mongo_host: str = os.getenv("MONGO_HOST_PROD")
    prod_mongo_port: int = int(os.getenv("MONGO_PORT_PROD", 27019))

    @property
    def mongo_uri(self) -> str:
        """
        Dynamically generate the MongoDB URI based on the selected environment.
        """
        if self.environment == "DEV":
            return f"mongodb://{self.dev_mongo_user}:{self.dev_mongo_password}@{self.dev_mongo_host}:{self.dev_mongo_port}"
        elif self.environment == "TEST":
            return f"mongodb://{self.test_mongo_user}:{self.test_mongo_password}@{self.test_mongo_host}:{self.test_mongo_port}"
        elif self.environment == "PROD":
            return f"mongodb://{self.prod_mongo_user}:{self.prod_mongo_password}@{self.prod_mongo_host}:{self.prod_mongo_port}"
        else:
            raise ValueError("Invalid environment. Choose DEV, TEST, or PROD.")

settings = Settings()


