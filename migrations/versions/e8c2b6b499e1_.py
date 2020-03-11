"""empty message

Revision ID: e8c2b6b499e1
Revises: 
Create Date: 2020-03-11 16:29:44.603420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8c2b6b499e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Frequencia',
    sa.Column('idFrequencia', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('idFrequencia')
    )
    op.create_table('Projeto',
    sa.Column('idProjeto', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('prazo', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('idProjeto')
    )
    op.create_table('Raridade',
    sa.Column('idRaridade', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('recompensa', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('idRaridade')
    )
    op.create_index(op.f('ix_Raridade_recompensa'), 'Raridade', ['recompensa'], unique=False)
    op.create_table('TipoUsuario',
    sa.Column('idTipoUsuario', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('idTipoUsuario')
    )
    op.create_table('Loja',
    sa.Column('idLoja', sa.Integer(), nullable=False),
    sa.Column('Projeto_idProjeto', sa.Integer(), nullable=True),
    sa.Column('dataAbertura', sa.DateTime(), nullable=False),
    sa.Column('dataFechamento', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['Projeto_idProjeto'], ['Projeto.idProjeto'], ),
    sa.PrimaryKeyConstraint('idLoja')
    )
    op.create_table('Tarefa',
    sa.Column('idTarefa', sa.Integer(), nullable=False),
    sa.Column('Projeto_idProjeto', sa.Integer(), nullable=True),
    sa.Column('Raridade_idRaridade', sa.Integer(), nullable=True),
    sa.Column('Frequencia_idFrequencia', sa.Integer(), nullable=True),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('prazo', sa.DateTime(), nullable=False),
    sa.Column('recompensa', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Frequencia_idFrequencia'], ['Frequencia.idFrequencia'], ),
    sa.ForeignKeyConstraint(['Projeto_idProjeto'], ['Projeto.idProjeto'], ),
    sa.ForeignKeyConstraint(['Raridade_idRaridade'], ['Raridade.idRaridade'], ),
    sa.PrimaryKeyConstraint('idTarefa'),
    sa.UniqueConstraint('nome'),
    sa.UniqueConstraint('recompensa')
    )
    op.create_table('Usuario',
    sa.Column('idUsuario', sa.Integer(), nullable=False),
    sa.Column('TipoUsuario_idTipoUsuario', sa.Integer(), nullable=True),
    sa.Column('nome', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('dataNascimento', sa.DateTime(), nullable=False),
    sa.Column('senha', sa.String(length=18), nullable=False),
    sa.Column('pontos', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['TipoUsuario_idTipoUsuario'], ['TipoUsuario.idTipoUsuario'], ),
    sa.PrimaryKeyConstraint('idUsuario')
    )
    op.create_index(op.f('ix_Usuario_email'), 'Usuario', ['email'], unique=True)
    op.create_table('Item',
    sa.Column('idItem', sa.Integer(), nullable=False),
    sa.Column('Loja_idLoja', sa.Integer(), nullable=True),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('valor', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Loja_idLoja'], ['Loja.idLoja'], ),
    sa.PrimaryKeyConstraint('idItem'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('Meta',
    sa.Column('idMeta', sa.Integer(), nullable=False),
    sa.Column('Tarefa_idTarefa', sa.Integer(), nullable=True),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('feito', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['Tarefa_idTarefa'], ['Tarefa.idTarefa'], ),
    sa.PrimaryKeyConstraint('idMeta')
    )
    op.create_index(op.f('ix_Meta_feito'), 'Meta', ['feito'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Meta_feito'), table_name='Meta')
    op.drop_table('Meta')
    op.drop_table('Item')
    op.drop_index(op.f('ix_Usuario_email'), table_name='Usuario')
    op.drop_table('Usuario')
    op.drop_table('Tarefa')
    op.drop_table('Loja')
    op.drop_table('TipoUsuario')
    op.drop_index(op.f('ix_Raridade_recompensa'), table_name='Raridade')
    op.drop_table('Raridade')
    op.drop_table('Projeto')
    op.drop_table('Frequencia')
    # ### end Alembic commands ###
