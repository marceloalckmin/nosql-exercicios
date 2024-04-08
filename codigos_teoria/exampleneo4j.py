from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

def create_and_return_example(tx, code, test_data):
        query = """
            CREATE(n:TEST{
                description: $test_data,
                code: $code
            })
        """
        result = tx.run(
            query, 
            test_data = test_data,
            code = code
        )

        try:
            return [{"test_data": row["n"]["description"]} for row in result]

        # Capture any errors along with the query and data for traceability

        except ServiceUnavailable as exception:

            print("{query} raised an error: \n {exception}".format(query=query, exception=exception))
            raise

def get_amount_data(tx):
    query = """
        MATCH(n) RETURN COUNT(n) AS amount;
    """
    try:
        result = tx.run(query)
        return [{
            'amount':row['amount']
        } for row in result]

    except ServiceUnavailable as exception:

        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))

        raise

uri = ""
user = ""
password = ""