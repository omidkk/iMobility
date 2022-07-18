import requests


class CityBikeService:
    @classmethod
    def get(cls):
        uri = "https://wegfinder.at/api/v1/stations"

        response = requests.get(uri)
        result = response.json()

        transformed_data = []
        for item in result:
            transformed_data.append(
                {
                    "id": item["id"],
                    "name": item["name"],
                    "active": True if item["status"] == "aktiv" else False,
                    "description": item["description"],
                    "boxes": item["boxes"],
                    "free_boxes": item["free_boxes"],
                    "free_bikes": item["free_bikes"],
                    "free_ratio": item["boxes"] - item["free_boxes"],
                    "coordinates": [item["longitude"], item["latitude"]],
                }
            )

        filtered_data = list(filter(lambda item: item["free_bikes"] > 0, transformed_data))

        sorted_data = sorted(filtered_data, key=lambda item: (-item["free_bikes"], item["name"]))

        for item in sorted_data:
            address = cls.fetch_address(item["coordinates"][1], item["coordinates"][0])
            item.update({"address": address})

        return sorted_data

    @classmethod
    def fetch_address(cls, latitude, longitude):
        urll = "https://api.i-mobility.at/routing/api/v1/nearby_address"
        params = {"latitude": latitude, "longitude": longitude}
        response = requests.get(urll, params=params)
        result = response.json()
        name = result["data"]["name"]
        return name
