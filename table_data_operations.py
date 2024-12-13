import requests

from bs4 import BeautifulSoup


class TableData:
    def remove_links(self, text):
        return ''.join(c for c in text if c not in '[]' and not c.isdigit())

    def load_table_data(self):
        url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table', {'class': 'wikitable'})
        for table in tables:
            caption = table.find('caption')
            if caption.get_text(strip=True) == "Programming languages used in most popular websites*":
                rows = table.find_all('tr')[1:]
                data = []
                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) == 6:
                        website = self.remove_links(cols[0].get_text(strip=True))
                        popularity = cols[1].get_text(strip=True).split()[0].split('[')[0].replace(',', '').replace('.', '')
                        front_end = self.remove_links(cols[2].get_text(strip=True))
                        back_end = self.remove_links(cols[3].get_text(strip=True))
                        database = self.remove_links(cols[4].get_text(strip=True))
                        notes = cols[5].get_text(strip=True)
                        data.append({
                            'website': website,
                            'popularity': int(popularity) if popularity.isdigit() else 0,
                            'front_end': front_end,
                            'back_end': back_end,
                            'database': database,
                            'notes': notes
                        })
                return data
        raise ValueError("Table with caption 'Programming languages used in most popular websites' not found")

    def popularity_should_be_greater_than_threshold(self, threshold, table_data):
        invalid_rows = []
        for row in table_data:
            if row['popularity'] < threshold:
                message = (
                    f"{row['website']} (Frontend:{row['front_end']}|"
                    f"Backend:{row['back_end']}) has "
                    f"{int(row['popularity']):,} unique visitors per month. "
                    f"(Expected more than {int(threshold):,})"
                )
                invalid_rows.append(message)
        assert not invalid_rows, "\n".join(invalid_rows)
