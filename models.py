{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "efa7227d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, UniqueConstraint\n",
    "from sqlalchemy.ext.declarative import declarative_base\n",
    "from sqlalchemy.orm import sessionmaker\n",
    "from datetime import datetime\n",
    "from sqlalchemy.orm import declarative_base\n",
    "\n",
    "# Define the database connection URL with the newly created database\n",
    "db_url_with_db = 'postgresql://rajsingh:[Raj];12@localhost:5432/rss_feed_database'\n",
    "\n",
    "# Create a new engine with the specified database name\n",
    "engine_with_db = create_engine(db_url_with_db)\n",
    "\n",
    "# Define the base class for ORM\n",
    "Base = declarative_base()\n",
    "\n",
    "# Define the Article model\n",
    "class Article(Base):\n",
    "    __tablename__ = 'articles'\n",
    "\n",
    "    id = Column(Integer, primary_key=True)\n",
    "    title = Column(String, nullable=False)\n",
    "    content = Column(Text)\n",
    "    publication_date = Column(TIMESTAMP)\n",
    "    source_url = Column(String)\n",
    "    \n",
    "    # Ensure each article is unique based on title and source URL\n",
    "    __table_args__ = (\n",
    "        UniqueConstraint('title', 'source_url', name='uq_title_source_url'),\n",
    "    )\n",
    "\n",
    "# Create the table in the database if it doesn't exist\n",
    "Base.metadata.create_all(engine_with_db)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c8c14d89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting psycopg2\n",
      "  Obtaining dependency information for psycopg2 from https://files.pythonhosted.org/packages/37/2c/5133dd3183a3bd82371569f0dd783e6927672de7e671b278ce248810b7f7/psycopg2-2.9.9-cp311-cp311-win_amd64.whl.metadata\n",
      "  Downloading psycopg2-2.9.9-cp311-cp311-win_amd64.whl.metadata (4.5 kB)\n",
      "Downloading psycopg2-2.9.9-cp311-cp311-win_amd64.whl (1.2 MB)\n",
      "   ---------------------------------------- 0.0/1.2 MB ? eta -:--:--\n",
      "   ---------------------------------------- 0.0/1.2 MB ? eta -:--:--\n",
      "   ---------------------------------------- 0.0/1.2 MB ? eta -:--:--\n",
      "   - -------------------------------------- 0.0/1.2 MB 495.5 kB/s eta 0:00:03\n",
      "   --- ------------------------------------ 0.1/1.2 MB 751.6 kB/s eta 0:00:02\n",
      "   ------ --------------------------------- 0.2/1.2 MB 1.3 MB/s eta 0:00:01\n",
      "   ---------- ----------------------------- 0.3/1.2 MB 1.6 MB/s eta 0:00:01\n",
      "   ------------- -------------------------- 0.4/1.2 MB 1.6 MB/s eta 0:00:01\n",
      "   ------------------------ --------------- 0.7/1.2 MB 2.6 MB/s eta 0:00:01\n",
      "   ---------------------------------------  1.2/1.2 MB 3.7 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 1.2/1.2 MB 3.5 MB/s eta 0:00:00\n",
      "Installing collected packages: psycopg2\n",
      "Successfully installed psycopg2-2.9.9\n"
     ]
    }
   ],
   "source": [
    "!pip install psycopg2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "a42d1058",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
