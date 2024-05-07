from neo4j import GraphDatabase


class Neo4jDB:

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create_player(self, player_id, player_name):
        self._write_transaction(self._create_player, player_id, player_name)

    def _create_player(self, tx, player_id, player_name):
        tx.run("CREATE (:Player {id: $id, name: $name})",
               id=player_id, name=player_name)

    def update_player(self, player_id, player_name):
        self._write_transaction(self._update_player, player_id, player_name)

    def _update_player(self, tx, player_id, player_name):
        tx.run("MATCH (p:Player {id: $id}) SET p.name = $name",
               id=player_id, name=player_name)

    def delete_player(self, player_id):
        self._write_transaction(self._delete_player, player_id)

    def _delete_player(self, tx, player_id):
        tx.run("MATCH (p:Player {id: $id}) DETACH DELETE p", id=player_id)

    def get_players(self):
        return self._read_transaction(self._get_players)

    def _get_players(self, tx):
        result = tx.run("MATCH (p:Player) RETURN p.id AS id, p.name AS name")
        return [dict(record) for record in result]

    def create_match(self, match_id, player_ids, result):
        self._write_transaction(
            self._create_match, match_id, player_ids, result)

    def _create_match(self, tx, match_id, player_ids, result):
        tx.run("CREATE (:Match {id: $id, player_ids: $player_ids, result: $result})", id=match_id,
               player_ids=player_ids, result=result)

    def get_match(self, match_id):
        return self._read_transaction(self._get_match, match_id)

    def _get_match(self, tx, match_id):
        result = tx.run("MATCH (m:Match {id: $id}) RETURN m.id AS id, m.player_ids AS player_ids, m.result AS result",
                        id=match_id)
        return dict(result.single())

    def delete_match(self, match_id):
        self._write_transaction(self._delete_match, match_id)

    def _delete_match(self, tx, match_id):
        tx.run("MATCH (m:Match {id: $id}) DETACH DELETE m", id=match_id)

    def update_match(self, match_id, result):
        self._write_transaction(self._update_match, match_id, result)

    def _update_match(self, tx, match_id, result):
        tx.run(
            "MATCH (m:Match {id: $id}) SET m.result = $result", id=match_id, result=result)

    def _read_transaction(self, func, *args, **kwargs):
        with self._driver.session() as session:
            result = session.read_transaction(func, *args, **kwargs)
            return result

    def _write_transaction(self, func, *args, **kwargs):
        with self._driver.session() as session:
            session.write_transaction(func, *args, **kwargs)