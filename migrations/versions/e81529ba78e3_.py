"""empty message

Revision ID: e81529ba78e3
Revises: 3ee6cc7271ba
Create Date: 2021-03-01 19:39:57.602258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e81529ba78e3'
down_revision = '3ee6cc7271ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('atuacoes_profissionais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('instituicao_id', sa.Integer(), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('termino', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['instituicao_id'], ['instituicoes.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('formacoes_complementares',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('instituicao_id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=200), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('termino', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['instituicao_id'], ['instituicoes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('atividades_profissionais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('atuacao_profissional_id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=200), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('termino', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['atuacao_profissional_id'], ['atuacoes_profissionais.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('formacoes_academicas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('curso_id', sa.Integer(), nullable=False),
    sa.Column('trabalho_conclusao', sa.String(length=200), nullable=True),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('termino', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['curso_id'], ['cursos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('formacoes_academicas')
    op.drop_table('atividades_profissionais')
    op.drop_table('formacoes_complementares')
    op.drop_table('atuacoes_profissionais')
    # ### end Alembic commands ###
