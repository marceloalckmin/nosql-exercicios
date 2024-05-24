from relatorio_8.gamedatabase import GraphDatabase


class GameDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_player(self, name):
        with self.driver.session() as session:
            query = "CREATE (p:Player {name: $name}) RETURN p.id as id"
            result = session.run(query, name=name)
            player_id = result.single()["id"]
            return player_id

    def update_player(self, player_id, name):
        with self.driver.session() as session:
            query = "MATCH (p:Player) WHERE p.id = $player_id SET p.name = $name"
            session.run(query, player_id=player_id, name=name)

    def delete_player(self, player_id):
        with self.driver.session() as session:
            query = "MATCH (p:Player) WHERE p.id = $player_id DETACH DELETE p"
            session.run(query, player_id=player_id)

    def get_players(self):
        with self.driver.session() as session:
            query = "MATCH (p:Player) RETURN p.id as id, p.name as name"
            result = session.run(query)
            players = [{"id": record["id"], "name": record["name"]}
                       for record in result]
            return players

    def create_match(self, player_ids, result):
        with self.driver.session() as session:
            query = "CREATE (m:Match {result: $result}) RETURN m.id as id"
            result = session.run(query, result=result)
            match_id = result.single()["id"]
            for player_id in player_ids:
                query = "MATCH (p:Player) WHERE p.id = $player_id CREATE (p)-[:PARTICIPATED_IN]->(m)"
                session.run(query, player_id=player_id)
            return match_id

    def get_match(self, match_id):
        with self.driver.session() as session:
            query = "MATCH (m:Match) WHERE m.id = $match_id RETURN m.result as result"
            result = session.run(query, match_id=match_id)
            match_record = result.single()
            if not match_record:
                return None
            result = match_record["result"]
            query = "MATCH (m:Match)-[:PARTICIPATED_IN]-(p:Player) WHERE m.id = $match_id RETURN p.id as id, p.name as name, m.result as result"
            players_result = session.run(query, match_id=match_id)
            players = [{"id": record["id"], "name": record["name"],
                        "result": record["result"]} for record in players_result]
            return {"id": match_id, "result": result, "players": players}

    def get_player_matches(self, player_id):
        with self.driver.session() as session:
            query = "MATCH (p:Player)-[:PARTICIPATED_IN]-(m:Match) WHERE p.id = $player_id RETURN m.id as id, m.result as result"
            result = session.run(query, player_id=player_id)
            matches = [{"id": record["id"], "result": record["result"]}
                       for record in result]
            return matches