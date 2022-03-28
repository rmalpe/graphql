# graphql

Query all posts

query AllPosts {
  listPosts {
    success
    errors
    posts {
      id
      title 
      description
      created_at
    }
  }
}


Querying a single post by id


query GetPost {
  getPost(id: "1") {
    post {
      id
      title
      description
    }
    success
    errors
  }
}


Mutation

Creating a new post
mutation CreateNewPost {
  createPost(
    title: "New Blog Post", 
    description:"Some Description") {
    post {
      id
      title
      description
      created_at
    }
    success
    errors
  }
}


Updating a post
mutation UpdatePost {
  updatePost(id:"2", title:"Hello title", description:"updated description") {
    post {
      id
      title
      description
    }
    success
    errors
  }
}


Deleting a post

mutation DeletePost {
  deletePost(id:"13") {
    success
    errors
      post{
        id
        title
        description
        created_at
      }
    }
}


