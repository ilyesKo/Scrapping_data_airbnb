import requests
from pathlib import Path
import logging


FILEPATH = Path(__file__).parent / "airbnb.html"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def fetch_content(url: str) -> str:
    """ fetch content of the page with given url """
    response = requests.get(url)
    return response.text


def _write_to_file(content: str) -> bool:
    """Write content to file"""

    logger.debug("Writing content to file")
    with open(FILEPATH, "w") as f:
        f.write(content)
    
    return FILEPATH.exists()

def _read_from_file() -> str:
    """Read content from file"""

    logger.debug("Reading content from file")

    with open(FILEPATH, "r") as f:
        return f.read()

if __name__ == '__main__':
    url = "https://www.airbnb.fr/s/Afrique/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-05-01&monthly_length=3&monthly_end_date=2024-08-01&price_filter_input_type=0&channel=EXPLORE&place_id=ChIJ1fWMlApsoBARs_CQnslwghA&date_picker_type=calendar&checkin=2024-04-12&checkout=2024-04-27&source=structured_search_input_header&search_type=filter_change"
    #fetch_content(url=url)
    print('filepath', FILEPATH)


