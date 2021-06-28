""" Módulo para salvar dados de uma busca em uma coleção no DynamoDB."""
import typing

import boto3

from botocore.exceptions import ClientError


TABLE_NAME = 'ArtistsTopSongs'


def create_song_list(artist: str, songs: typing.List[str], id_transacao: str):
    """
    Cria lista com resultados da consulta da API do Genius no DynamoDB

    Args:
        artist (str): Nome do artist buscado.
        songs (list): Lista com as 10 músicas mais populares do artista.
        id_transacao (str): id de transação no formato uuid versão 4.
    """

    songs = songs or []
    try:
        table = boto3.resource('dynamodb').Table(TABLE_NAME)
        table.put_item(
            Item={
                "Artist": artist,
                "Songs": songs,
                "Id": id_transacao
            },
            ConditionExpression=boto3.dynamodb.conditions.Attr(
                "Artist").not_exists()
        )
    except ClientError as error:
        if error.response['Error']['Code'] == 'ConditionalCheckFailedException':
            raise ValueError("Artista já existente") from error
