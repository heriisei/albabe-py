"""empty message

Revision ID: 416159c4e639
Revises: 
Create Date: 2019-01-06 18:14:13.757654

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '416159c4e639'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_fakultas',
    sa.Column('id_fakultas', sa.Integer(), nullable=False),
    sa.Column('nama_fakultas', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id_fakultas')
    )
    op.create_index(op.f('ix_tb_fakultas_nama_fakultas'), 'tb_fakultas', ['nama_fakultas'], unique=False)
    op.create_table('tb_jurusan',
    sa.Column('id_jurusan', sa.Integer(), nullable=False),
    sa.Column('nama_jurusan', sa.Integer(), nullable=True),
    sa.Column('id_fakultas', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_fakultas'], ['tb_fakultas.id_fakultas'], ),
    sa.PrimaryKeyConstraint('id_jurusan')
    )
    op.create_index(op.f('ix_tb_jurusan_nama_jurusan'), 'tb_jurusan', ['nama_jurusan'], unique=False)
    op.create_table('tb_users',
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('useremail', sa.String(length=60), nullable=True),
    sa.Column('nama_depan', sa.String(length=60), nullable=True),
    sa.Column('nama_belakang', sa.String(length=60), nullable=True),
    sa.Column('tgl_lahir', sa.Date(), nullable=True),
    sa.Column('no_hp', sa.String(length=20), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('id_jurusan', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_jurusan'], ['tb_jurusan.id_jurusan'], ),
    sa.PrimaryKeyConstraint('id_user')
    )
    op.create_index(op.f('ix_tb_users_nama_belakang'), 'tb_users', ['nama_belakang'], unique=False)
    op.create_index(op.f('ix_tb_users_nama_depan'), 'tb_users', ['nama_depan'], unique=False)
    op.create_index(op.f('ix_tb_users_useremail'), 'tb_users', ['useremail'], unique=True)
    op.create_index(op.f('ix_tb_users_username'), 'tb_users', ['username'], unique=True)
    op.create_table('tb_barang',
    sa.Column('id_barang', sa.Integer(), nullable=False),
    sa.Column('nama_barang', sa.String(length=60), nullable=True),
    sa.Column('harga_barang', sa.Integer(), nullable=True),
    sa.Column('garansi_barang', sa.Boolean(), nullable=True),
    sa.Column('foto_barang', sa.String(), nullable=True),
    sa.Column('id_user', sa.Integer(), nullable=True),
    sa.Column('id_jurusan', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_jurusan'], ['tb_jurusan.id_jurusan'], ),
    sa.ForeignKeyConstraint(['id_user'], ['tb_users.id_user'], ),
    sa.PrimaryKeyConstraint('id_barang')
    )
    op.create_index(op.f('ix_tb_barang_foto_barang'), 'tb_barang', ['foto_barang'], unique=False)
    op.create_index(op.f('ix_tb_barang_harga_barang'), 'tb_barang', ['harga_barang'], unique=False)
    op.create_index(op.f('ix_tb_barang_nama_barang'), 'tb_barang', ['nama_barang'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tb_barang_nama_barang'), table_name='tb_barang')
    op.drop_index(op.f('ix_tb_barang_harga_barang'), table_name='tb_barang')
    op.drop_index(op.f('ix_tb_barang_foto_barang'), table_name='tb_barang')
    op.drop_table('tb_barang')
    op.drop_index(op.f('ix_tb_users_username'), table_name='tb_users')
    op.drop_index(op.f('ix_tb_users_useremail'), table_name='tb_users')
    op.drop_index(op.f('ix_tb_users_nama_depan'), table_name='tb_users')
    op.drop_index(op.f('ix_tb_users_nama_belakang'), table_name='tb_users')
    op.drop_table('tb_users')
    op.drop_index(op.f('ix_tb_jurusan_nama_jurusan'), table_name='tb_jurusan')
    op.drop_table('tb_jurusan')
    op.drop_index(op.f('ix_tb_fakultas_nama_fakultas'), table_name='tb_fakultas')
    op.drop_table('tb_fakultas')
    # ### end Alembic commands ###
