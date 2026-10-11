package sodartl.util

import scala.collection.mutable 

object DepthFirstSearch{
  type Graph[A] = Map[A, Seq[A]]

  def traverse[A](graph: Graph[A], start: A): Vector[A] = {
    val visited = mutable.LinkedHashSet.empty[A]

    def dfs(node:A): Unit={
      if (visited.contains(node)){
        return
      }
      visited += node 
      graph.getorElse(node, Seq.empty).foreach(dfs)

    }
    dfs(start)
    visited.toVector
  }
}

