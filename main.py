import os

import click
from autorag.evaluator import Evaluator

root_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(root_path, 'data')


@click.command()
@click.option('--config', type=click.Path(exists=True))
@click.option('--qa_data_path', type=click.Path(exists=True), default=os.path.join(data_path, 'qa.parquet'))
@click.option('--corpus_data_path', type=click.Path(exists=True), default=os.path.join(data_path, 'corpus.parquet'))
def main(config):
    evaluator = Evaluator(qa_data_path=os.path.join(data_path, 'qa_test.parquet'),
                          corpus_data_path=os.path.join(data_path, 'corpus.parquet'))
    evaluator.start_trial(config)


if __name__ == '__main__':
    main()
