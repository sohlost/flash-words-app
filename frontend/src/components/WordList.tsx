'use client'

import React, { useState, useEffect } from 'react'
import styles from './WordList.module.css'

interface Word {
  id: string
  word: string
  definition: string
  example: string
}

export default function WordList() {
  const [words, setWords] = useState<Word[]>([])
  const [newWord, setNewWord] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchWords()
  }, [])

  const fetchWords = async () => {
    try {
      const response = await fetch('/api/words')
      if (!response.ok) throw new Error('Failed to fetch words')
      const data = await response.json()
      setWords(data)
    } catch (error) {
      setError('Error fetching words. Please try again later.')
      console.error('Error fetching words:', error)
    }
  }

  const addWord = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!newWord.trim()) return

    setIsLoading(true)
    setError(null)
    try {
      const response = await fetch('/api/words', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ word: newWord }),
      })
      if (!response.ok) throw new Error('Failed to add word')
      const addedWord = await response.json()
      setWords([...words, addedWord])
      setNewWord('')
    } catch (error) {
      setError('Error adding word. Please try again.')
      console.error('Error adding word:', error)
    } finally {
      setIsLoading(false)
    }
  }

  const deleteWord = async (id: string) => {
    setError(null)
    try {
      const response = await fetch(`/api/words/${id}`, { method: 'DELETE' })
      if (!response.ok) throw new Error('Failed to delete word')
      setWords(words.filter(word => word.id !== id))
    } catch (error) {
      setError('Error deleting word. Please try again.')
      console.error('Error deleting word:', error)
    }
  }

  const regenerateWord = async (id: string) => {
    setIsLoading(true)
    setError(null)
    try {
      const response = await fetch(`/api/words/${id}/regenerate`, { method: 'POST' })
      if (!response.ok) throw new Error('Failed to regenerate word')
      const updatedWord = await response.json()
      setWords(words.map(word => word.id === id ? updatedWord : word))
    } catch (error) {
      setError('Error regenerating word. Please try again.')
      console.error('Error regenerating word:', error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>My Word List</h1>
      <form onSubmit={addWord} className={styles.form}>
        <input
          type="text"
          value={newWord}
          onChange={(e) => setNewWord(e.target.value)}
          placeholder="Enter a new word"
          className={styles.input}
        />
        <button type="submit" disabled={isLoading} className={styles.button}>
          {isLoading ? 'Adding...' : 'Add Word'}
        </button>
      </form>
      {error && <p className={styles.error}>{error}</p>}
      <div className={styles.wordList}>
        {words.map((word) => (
          <div key={word.id} className={styles.wordCard}>
            <h2 className={styles.wordTitle}>{word.word}</h2>
            <p className={styles.wordDefinition}><strong>Definition:</strong> {word.definition}</p>
            <p className={styles.wordExample}><strong>Example:</strong> {word.example}</p>
            <div className={styles.buttonGroup}>
              <button onClick={() => deleteWord(word.id)} className={`${styles.button} ${styles.deleteButton}`}>
                Delete
              </button>
              <button onClick={() => regenerateWord(word.id)} disabled={isLoading} className={styles.button}>
                Regenerate
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}